.PHONY: clean-pyc env test coverage

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

env:
	export FLASK_APP=manage.py

test:
	@pytest tests
