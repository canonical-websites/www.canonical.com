SHELL := /bin/bash

develop:
	bundle exec sass --watch templates/static/css/styles.scss:templates/static/css/styles.css &
	./manage.py runserver_plus

setup: setup-venv setup-ruby

setup-ruby:
	##
	# Install dependencies
	##
	if [ ! $$(command -v bundle) ]; then sudo apt-get install bundler; fi

	##
	# Install gem dependencies
	##
	bundle update


setup-venv:
	##
	# Install virtualenv dependencies
	##
	if [ ! $$(command -v pip) ]; then sudo apt-get install python-pip; fi
	if [ ! $$(command -v virtualenv) ]; then sudo apt-get install python-virtualenv; fi

	##
	# Make virtualenv directory if it doesn't exist
	##
	if [ ! -d "env" ]; then virtualenv env; fi

	##
	# Install python dependencies
	##
	env/bin/pip install -r dev_requirements.txt

	##
	#
	# Now run:
	#
	# > source env/bin/activate
	#
	# And when you're done:
	#
	# > deactivate
	#
	##
