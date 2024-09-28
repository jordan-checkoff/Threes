.PHONY: run, clean, test, setup

run:
	./venv/bin/python3 src/app.py

clean:
	pyclean .
	rm -rf venv

test:
	PYTHONPATH="src" ./venv/bin/python3 -m unittest discover -s ./test/model

setup:
	make venv/bin/activate

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt