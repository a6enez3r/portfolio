ip := wsgi
ep := ${ip}.py
mn := src
tmn := tests
default_port := 5000
ifeq ($(port),)
port := ${default_port}
endif
ifeq ($(version),)
version := 0.0.1
endif
ifeq ($(cm),)
cm := default commit message
endif
ifeq ($(branch),)
branch := main
endif
ifeq ($(deptype),)
deptype := development
endif
ifeq ($(flask_env),)
flask_env := development
endif
ifeq ($(docker_env),)
docker_env := development
endif
ifeq ($(cname),)
cname := portfolio_${docker_env}
endif
ifeq ($(ctag),)
ctag := latest
endif

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


TARGET_MAX_CHAR_NUM=20
## show help
help:
	@echo ''
	@echo 'usage:'
	@echo '  ${BLUE}make${RESET} ${RED}<cmd>${RESET}'
	@echo ''
	@echo 'cmds:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${PURPLE}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

# SCM #

## save changes locally using git
save-local:
	@echo "saving..."
	@git add .
	@git commit -m "${cm}"

## save changes to remote using git
save-remote:
	@echo "saving to remote..."
	@git push origin ${branch}

## pull changes from remote
pull-remote:
	@echo "pulling from remote..."
	@git merge origin ${branch}

## create new tag, recreate if it exists
tag:
	git tag -d ${version} || : 
	git push --delete origin ${version} || : 
	git tag -a ${version} -m "latest" 
	git push origin --tags
#######

# DEV #

## install dependencies [deptype = dev | prod] 
install:
	@echo "dep type: ${deptype}"
	@python3 -m pip install --upgrade pip
	@python3 -m pip install -r $(CURDIR)/requirements/${deptype}.txt

## show app routes
routes:
	@echo "flask env: ${flask_env}"
	@FLASK_APP=${ep} FLASK_ENV=${flask_env} ENVIRONMENT=${flask_env} PORT=${port} python3 -m flask routes

## run app [env = development | production]
run:
	@echo "flask env: ${flask_env}"
ifeq ($(flask_env),production)
	@echo "using: gunicorn"
	@gunicorn --workers 4 --bind 0.0.0.0:5000 ${ip}:app
endif
ifeq ($(flask_env),development)
	@echo "using: flask"
	@FLASK_APP=${ep} FLASK_ENV=${flask_env} ENVIRONMENT=${flask_env} PORT=${port} python3 -m flask run --host=0.0.0.0 --no-reload
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
	@FLASK_APP=${ep} FLASK_ENV=testing ENVIRONMENT=testing PORT=${port} pytest --cov-report term-missing --durations=10 --cov=${mn} ${tmn} -v
	@sleep 2.5
	@rm -f .coverage*

## run load tests [pytest + locust]
load-test:
	@make run & locust -f $(CURDIR)/tests/test_load.py

## build docker env
build-env:
	@docker build -f ./dockerfiles/Dockerfile.${docker_env} . -t ${cname}:${ctag}

## start docker env
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

## init env + install common tools
init-env:
	apt-get update && apt-get -y upgrade
	apt-get install curl sudo bash vim ncurses-bin -y
	apt-get install build-essential python3-pip -y --no-install-recommends
#######