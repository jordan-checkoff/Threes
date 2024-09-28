.PHONY: run, clean, test

run: venv/bin/activate
	./venv/bin/python3 src/app.py

test: venv/bin/activate
	PYTHONPATH="src" ./venv/bin/python3 -m unittest discover -s ./test/model

clean:
	pyclean .
	rm -rf venv

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt