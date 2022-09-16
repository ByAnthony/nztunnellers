install:
	pip install -r requirements.txt

install-dev: install
	pip install -r requirements-dev.txt

test-server:
	pytest -v ./server

dev:
	DEV=true python server/run.py