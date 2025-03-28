dev-start:
	python manage.py runserver --settings=config.settings.dev

dev-migrate:
	python manage.py migrate --settings=config.settings.dev