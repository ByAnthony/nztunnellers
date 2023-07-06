install:
	pip install -r requirements.txt

install-dev: install
	pip install -r requirements-dev.txt

test-server:
	python3 -m coverage run -m pytest ./server
	python3 -m coverage report -m

dev:
	DEV=true python -m server.run
