.PHONY: run, clean, test, setup

run: setup
	./venv/bin/python3 src/app.py

test: setup
	PYTHONPATH="src" ./venv/bin/python3 -m unittest discover -s ./test/model

clean:
	pyclean .
	rm -rf venv

setup: venv/bin/activate

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt