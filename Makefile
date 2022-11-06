install:
	pip install -r requirements.txt

install-dev: install
	pip install -r requirements-dev.txt

test-server:
	pytest -vv ./server

dev:
	DEV=true python -m server.run
