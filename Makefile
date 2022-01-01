ip := wsgi
ep := ${ip}.py
mn := src
tmn := tests

# flask
default_port := 5000
ifeq ($(port),)
port := ${default_port}
endif
default_host := 0.0.0.0
ifeq ($(host),)
host := ${default_host}
endif
# git
ifeq ($(version),)
version := 0.0.1
endif
ifeq ($(cm),)
cm := default commit message
endif
ifeq ($(branch),)
branch := main
endif
# python / docker / dep
ifeq ($(dtype),)
dtype := development
endif
ifeq ($(fenv),)
fenv := development
endif
ifeq ($(denv),)
denv := development
endif
ifeq ($(cname),)
cname := teret_${denv}
endif
ifeq ($(ctag),)
ctag := latest
endif
# pytest
ifeq ($(topts),)
topts := -vv
endif

.DEFAULT_GOAL := help
TARGET_MAX_CHAR_NUM=20
# COLORS
ifneq (,$(findstring xterm,${TERM}))
	BLACK        := $(shell tput -Txterm setaf 0 || exit 0)
	RED          := $(shell tput -Txterm setaf 1 || exit 0)
	GREEN        := $(shell tput -Txterm setaf 2 || exit 0)
	YELLOW       := $(shell tput -Txterm setaf 3 || exit 0)
	LIGHTPURPLE  := $(shell tput -Txterm setaf 4 || exit 0)
	PURPLE       := $(shell tput -Txterm setaf 5 || exit 0)
	BLUE         := $(shell tput -Txterm setaf 6 || exit 0)
	WHITE        := $(shell tput -Txterm setaf 7 || exit 0)
	RESET := $(shell tput -Txterm sgr0)
else
	BLACK        := ""
	RED          := ""
	GREEN        := ""
	YELLOW       := ""
	LIGHTPURPLE  := ""
	PURPLE       := ""
	BLUE         := ""
	WHITE        := ""
	RESET        := ""
endif

## show usage / common commands available
.PHONY: help
help:
	@printf "${RED}cmds:\n\n";

	@awk '{ \
			if ($$0 ~ /^.PHONY: [a-zA-Z\-\_0-9]+$$/) { \
				helpCommand = substr($$0, index($$0, ":") + 2); \
				if (helpMessage) { \
					printf "  ${PURPLE}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n\n", helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^[a-zA-Z\-\_0-9.]+:/) { \
				helpCommand = substr($$0, 0, index($$0, ":")); \
				if (helpMessage) { \
					printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
					helpMessage = ""; \
				} \
			} else if ($$0 ~ /^##/) { \
				if (helpMessage) { \
					helpMessage = helpMessage"\n                     "substr($$0, 3); \
				} else { \
					helpMessage = substr($$0, 3); \
				} \
			} else { \
				if (helpMessage) { \
					print "\n${LIGHTPURPLE}             "helpMessage"\n" \
				} \
				helpMessage = ""; \
			} \
		}' \
		$(MAKEFILE_LIST)

## -- git --

## save changes locally [git]
save-local:
	@echo "saving..."
	@git add .
	@git commit -m "${cm}"

## save changes to remote [git]
save-remote:
	@echo "saving to remote..."
	@git push origin ${branch}

## pull changes from remote [git]
pull-remote:
	@echo "pulling from remote..."
	@git merge origin ${branch}

## create new tag, recreate if it exists [git]
tag:
	git tag -d ${version} || : 
	git push --delete origin ${version} || : 
	git tag -a ${version} -m "latest" 
	git push origin --tags

## -- python --

## install dependencies [dtype = development | production] 
deps:
	@echo "dep type: ${dtype}"
	@python3 -m pip install --upgrade pip setuptools wheel
	@python3 -m pip install -r $(CURDIR)/requirements/${dtype}.txt

## show app routes [fenv = development | production]
routes:
	@echo "flask env: ${fenv}"
	@FLASK_APP=${ep} fenv=${fenv} ENVIRONMENT=${fenv} PORT=${port} python3 -m flask routes

## run app [fenv = development | production]
run:
	@echo "flask env: ${fenv}"
ifeq ($(fenv),production)
	@echo "using: gunicorn"
	@gunicorn --workers 1 --bind ${host}:${port} ${ip}:app
endif
ifeq ($(fenv),development)
	@echo "using: flask"
	@FLASK_APP=${ep} FLASK_ENV=${fenv} ENVIRONMENT=${fenv} PORT=${port} python3 -m flask run --host=${host} --port=${port} --no-reload
endif

## run formatting [black]
format:
	@python3 -m black ${mn}
	@python3 -m black ${tmn}

## run linting [pylint]
lint:
	@python3 -m pylint ${mn}
	@python3 -m pylint ${tmn}

## run tests [pytest]
test:
	@FLASK_APP=${ep} FLASK_ENV=testing ENVIRONMENT=testing PORT=${port} pytest --cov-report term-missing --durations=10 --cov=${mn} ${tmn} ${topts}
	@sleep 1
	@rm -f .coverage*

## run load tests [pytest + locust]
load-test:
	@make run & locust -f $(CURDIR)/tests/test_load.py

## -- docker --

## build docker env [denv = development | production]
build-env:
	@docker build -f ./dockerfiles/Dockerfile.${denv} . -t ${cname}:${ctag}

## start docker env [denv = development | production]
up-env: build-env
	$(eval cid = $(shell (docker ps -aqf "name=${cname}")))
	$(if $(strip $(cid)), \
		@echo "existing container found. please run make purge-env",\
		@docker run -p ${port}:5000 --name ${cname} ${cname}:${ctag})
	$(endif)

## exec. into docker env
exec-env:
	$(eval cid = $(shell (docker ps -aqf "name=${cname}")))
	$(if $(strip $(cid)), \
		@echo "exec into env container..." && docker exec -it ${cid} bash,\
		@echo "env container not running.")
	$(endif)

## remove docker env
purge-env:
	$(eval cid = $(shell (docker ps -aqf "name=${cname}")))
	$(if $(strip $(cid)), \
		@echo "purging container..." && docker stop ${cid} && docker rm ${cid},\
		@echo "env container not running.")
	$(endif)

## get status of docker env
status-env:
	$(eval cid = $(shell (docker ps -aqf "name=${cname}")))
	$(if $(strip $(cid)), \
		@echo "env container running",\
		@echo "env container not running.")
	$(endif)

## init Linux env / install common tools
init-env:
	apt-get update && apt-get -y upgrade
	apt-get install curl sudo bash vim ncurses-bin -y
	apt-get install build-essential python3-pip -y --no-install-recommends
