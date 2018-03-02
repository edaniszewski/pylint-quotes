release:
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*
	rm -rf build/ dist/ pylint_quotes.egg-info/


coverage:
	pytest --verbose --cov-report term --cov-report xml --cov=pylint_quotes tests