install:
	pip install -r requirements.txt

install-dev:
	install
	pip install -r requirements-dev.txt

freeze:
	pip freeze > requirements-dev.txt
	pip freeze > requirements.txt

install-client:
	cd ./client && npm ci

test-client:
	cd ./client && npm run test

test-client-ci:
	cd ./client && npm run test:ci

test-server:
	python3 -m coverage run -m pytest ./server
	python3 -m coverage report -m --omit="*/__init__.py,server/db/models/*.py,server/models/*.py,*/test_*.py"

run-client:
	cd ./client && npm start

run-server:
	. server/venv/bin/activate
	DEV=true python -m server.run
