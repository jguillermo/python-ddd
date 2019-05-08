.DEFAULT_GOAL := help

## GENERAL ##
OWNER 			= guillermo
SERVICE_NAME 	= reto_api
PATH_PREFIX 	= "/v1"

## DEPLOY ##
ENV 			?= dev

## RESULT_VARS ##
PROJECT_NAME	= $(OWNER)-$(ENV)-$(SERVICE_NAME)
export CONTAINER_NAME 	= $(PROJECT_NAME)_backend
export CONTAINER_DB_NAME 	= $(PROJECT_NAME)_db
export IMAGE_DEV		= $(PROJECT_NAME):dev

## Target Commons ##

install: ## build image to dev: make build
	make build
	docker build -f docker/raml/Dockerfile -t $(IMAGE_RAML) docker/raml/

build: ## build image to dev: make build
	cp app/requirements.txt docker/dev/resources/requirements.txt
	docker build -f docker/dev/Dockerfile -t $(IMAGE_DEV) docker/dev/
	rm -f docker/dev/resources/requirements.txt

up: ## up docker containers: make up
	make set-config-local
	docker-compose up -d
	@make status

start: ## up docker containers: make up
	make up

down: ## Stops and removes the docker containers: make down
	docker-compose down

status: ## Show containers status: make status
	docker-compose ps

stop: ## Stops and removes the docker containers, use me with: make down
	docker-compose stop

restart: ## Restart all containers, use me with: make restart
	make down
	make start
	make status

ssh: ## Connect to container for ssh protocol : make ssh
	docker exec -it $(CONTAINER_NAME) bash

set-config-local: ## copia el archivo config/env.local al config : make set-config-local
	cp ${PWD}/app/config/config.env.local ${PWD}/app/config/config.env
	mkdir -p ${PWD}/app/files && chmod 777 ${PWD}/app/files

log: ## Show container logs make : make log
	docker-compose logs -f

log-backend: ## Show container logs make : make log
	docker-compose logs -f backend


stats: ## Show container logs make : make stats
	docker stats $(CONTAINER_NAME)

tests: ## Run the unitTests : make tests
	rm -rf $(PWD)/app/cover
	@docker run --rm -t -v $(PWD)/app:/app:rw --entrypoint /resources/test.sh $(IMAGE_DEV)

## Migrate DB##

migrate: ## Execute migrate : make migrate
	docker exec $(CONTAINER_NAME) /resources/alembic.sh upgrade head

migrate-info: ## Execute migrate : make migrate
	docker exec $(CONTAINER_NAME) /resources/alembic.sh upgrade head --sql

revision: ## Create a new revision : make revision
	docker exec $(CONTAINER_NAME) /resources/alembic.sh revision --autogenerate -m "migrate"
	#@sudo chown -R $(USER) $(PWD)/app/alembic/versions

downgrade: ## Execute migrate : make downgrade
	@docker exec $(CONTAINER_NAME) /resources/alembic.sh downgrade base

migrate-id: ## Execute migrate : make migrate-id
	@docker exec $(CONTAINER_NAME) /resources/alembic.sh upgrade $(ID)

dump: ## Execute migrate : make migrate
	docker exec $(CONTAINER_DB_NAME) /tmp/dump.sh

docker-kill: ## Execute migrate : make migrate
	docker rm -f $$(docker ps -aq)

## Target Help ##

help:
	@printf "\033[31m%-16s %-59s %s\033[0m\n" "Target" "Help" "Usage"; \
	printf "\033[31m%-16s %-59s %s\033[0m\n" "------" "----" "-----"; \
	grep -hE '^\S+:.*## .*$$' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' | sort | awk 'BEGIN {FS = ":"}; {printf "\033[32m%-16s\033[0m %-58s \033[34m%s\033[0m\n", $$1, $$2, $$3}'
