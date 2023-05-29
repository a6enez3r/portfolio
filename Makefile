ip := wsgi
ep := ${ip}.py
mn := portfolio
tn := tests

ifeq ($(version),)
version := 0.0.1
endif
ifeq ($(commit_message),)
commit_message := default commit message
endif
ifeq ($(branch),)
branch := main
endif
ifeq ($(pytest_opts),)
pytest_opts := -vv
endif
ifeq ($(dep_type),)
dep_type := development
endif
ifeq ($(container_tag),)
container_tag := ${dep_type}
endif
ifeq ($(durations),)
durations := 10
endif
ifeq ($(pkg_type),)
pkg_type := develop
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
	@git commit -m "${commit_message}"

## save changes to remote [git]
save-remote:
	@echo "saving to remote..."
	@git push origin ${branch}

## pull changes from remote
pull-remote:
	@echo "pulling from remote..."
	@git pull origin ${branch}

## create new tag, recreate if it exists
tag:
	@git tag -d ${version} || : 
	@git push --delete origin ${version} || : 
	@git tag -a ${version} -m "latest version" 
	@git push origin --tags

## -- python --

## build package
pkg-build:
	@echo "building..." && python3 setup.py build

## install package [pkg_type = editable | noneditable]
pkg-install:
	@echo "installing..." && python3 setup.py ${pkg_type}

## install package dependencies [dep_type = development | production]
deps:
	@python3 -m pip install --upgrade pip setuptools wheel
#	@python3 -m pip install .
	@if [ -f requirements/${dep_type}.txt ]; then pip install -r requirements/${dep_type}.txt; fi

## run tests [pytest]
test:
	@echo "running tests..."
	@python3 -m pytest --durations=${durations} --cov-report term-missing --cov=${mn} ${tn} ${pytest_opts}

## run load tests [pytest + locust]
load-test:
	@make run & locust -f $(CURDIR)/tests/test_load.py

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

## -- code quality --

## run test profiling [pytest-profiling]
profile:
	@echo "running tests..."
	@python3 -m pytest --profile ${tn} ${pytest_opts}

## run formatting [black]
format:
	@echo "formatting..."
	@python3 -m isort ${mn}
	@python3 -m isort ${tn}
	@sort-requirements requirements/development.txt
	@sort-requirements requirements/production.txt
	@python3 -m black ${mn}
	@python3 -m black ${tn}

## run linting [pylint]
lint:
	@echo "linting..."
	@python3 -m pylint ${mn}
	@python3 -m pylint ${tn}

## run linting & formatting
prettify: format lint

## type inference [pyre]
type-infer:
	@echo "inferring types..."
	@pyre infer

## type checking [pyre]
type-check:
	@echo "checking types..."
	@pyre

## scan for dead code [vulture]
scan-deadcode:
	@echo "checking dead code..."
	@vulture ${mn} || exit 0
	@vulture ${tn} || exit 0

## scan for security issues [bandit]
scan-security:
	@echo "checking for security issues..."
	@bandit ${mn}

## -- docs --

## build docs [pdoc]
docs-build:
	@echo "building docs..."
	@python3 -m pdoc ${mn} -o docs

## serve docs [pdoc]
docs-serve:
	@python3 -m pdoc ${mn}

## -- docker --

## build docker env [docker_env = development | production]
build-env:
	@docker build -f ./dockerfiles/Dockerfile.${docker_env} . -t ${container_name}:${container_tag}

## build & push image
push-env:
	@make build-env docker_env=production container_name="ghcr.io/a6enez3r/portfolio" container_tag="latest"
	@docker push ghcr.io/a6enez3r/portfolio

## start docker env [docker_env = development | production]
up-env: build-env
	$(eval cid = $(shell (docker ps -aqf "name=${container_name}")))
	$(if $(strip $(cid)), \
		@echo "existing container found. please run make purge-env",\
		@docker run -p ${port}:5000 --name ${container_name} ${container_name}:${container_tag})
	$(endif)

## exec. into docker env
exec-env:
	$(eval cid = $(shell (docker ps -aqf "name=${container_name}")))
	$(if $(strip $(cid)), \
		@echo "exec into env container..." && docker exec -it ${cid} bash,\
		@echo "env container not running.")
	$(endif)

## remove docker env
purge-env:
	$(eval cid = $(shell (docker ps -aqf "name=${container_name}")))
	$(if $(strip $(cid)), \
		@echo "purging container..." && docker stop ${cid} && docker rm ${cid},\
		@echo "env container not running.")
	$(endif)

## get status of docker env
status-env:
	$(eval cid = $(shell (docker ps -aqf "name=${container_name}")))
	$(if $(strip $(cid)), \
		@echo "env container running",\
		@echo "env container not running.")
	$(endif)

## init Linux env / install common tools
init-env:
	apt-get update && apt-get -y upgrade
	apt-get install curl sudo bash vim ncurses-bin -y
	apt-get install build-essential python3-pip -y --no-install-recommends
