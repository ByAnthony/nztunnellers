install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

freeze:
	pip freeze > requirements-dev.txt
	pip freeze > requirements.txt

typecheck:
	npm run typecheck --prefix client

install-client:
	npm ci --prefix client

test-client:
	npm run test --prefix client

test-client-ci:
	npm run test:ci --prefix client

test-server:
	python3 -m coverage run -m pytest ./server
	python3 -m coverage report -m --omit="*/__init__.py,server/db/models/*.py,server/models/*.py,*/test_*.py"

run-client:
	npm start --prefix client

run-server:
	. server/venv/bin/activate
	DEV=true python -m server.run
