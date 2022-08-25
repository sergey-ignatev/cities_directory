# Initial prepares

TERMINAL_CHECK := $(shell if [ -t 0 ] ; then echo terminal; else echo "not a terminal"; fi)

ifneq ($(strip $(shell pwd)),/app)
ifeq ($(strip $(CI)),)

ifeq ($(TERMINAL_CHECK), terminal)
	CMD_PREFIX := docker exec -ti citiesdirectory_web_1
else
	CMD_PREFIX := docker exec -i citiesdirectory_web_1
endif
endif
endif

# Helper command

help:
	@echo 'Test project'
	@echo ''
	@echo 'Commands:'
	@echo '    help - show this message'
	@echo ''
	@echo '    init-admin  - create default superuser (username: admin, password: password)'


# Usability functions

up:
	@docker-compose stop
	@docker-compose up -d

stop:
	@docker-compose stop


# Project initialization

init:
	@$(CMD_PREFIX) python3 manage.py makemigrations
	@sleep 3
	@$(CMD_PREFIX) python3 manage.py migrate
	@sleep 5
	@$(MAKE) init-admin
	@sleep 2
	@$(MAKE) fixture_migrate

init-admin:
	@$(CMD_PREFIX) python3 manage.py shell -c "from django.contrib.auth import get_user_model; USER = get_user_model(); USER.objects.filter(username='admin').exists() or USER.objects.create_superuser(username='admin', password='password')"

fixture_migrate:
	@$(CMD_PREFIX) python3 manage.py loaddata NewsFeedModel.json
	@$(CMD_PREFIX) python3 manage.py loaddata CommentRatingModel.json
