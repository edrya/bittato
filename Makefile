SHELL = /bin/bash
VE ?= ./ve
PIP ?= $(VE)/bin/pip
REQUIREMENTS ?= requirements.txt


create:
	@echo "Installing python virtual env at $(VE)"
	rm -rf $(VE)
	python3 -m venv $(VE)
	$(PIP) install --requirement $(REQUIREMENTS)

initdb:
	$(VE)/bin/flask db init
	$(VE)/bin/flask db migrate

runserver:
	$(VE)/bin/flask run