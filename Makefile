# Makefile for creating Pythonic Git Flow.
#
# Author:: Greg Albrecht <mailto:gba@splunk.com>
# Copyright:: Copyright 2012 Splunk, Inc.
# License:: Apache License 2.0
#


.DEFAULT: init


develop: 
	python setup.py develop

init:
	pip install -r requirements.txt --use-mirrors

lint:
	pylint -f parseable -i y -r n *.py | \
		tee pylint.log

flake8:
	flake8 --exit-zero  --max-complexity 12 *.py | \
		awk -F\: '{printf "%s:%s: [E]%s\n", $$1, $$2, $$3}' | tee flake8.log

pep8: flake8

clonedigger:
	clonedigger --cpd-output .

nosetests:
	nosetests

test: init lint flake8 clonedigger nosetests

clean:
	rm -rf *.egg* build dist *.pyc *.pyo cover doctest_pypi.cfg nosetests.xml \
		pylint.log *.egg output.xml flake8.log output.xml */*.pyc nohup.out

install:
	python setup.py install

uninstall:
	pip uninstall pygitflow
