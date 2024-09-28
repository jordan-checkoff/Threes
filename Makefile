.PHONY: run, clean, test

run:
	PYTHONPATH=src ./venv/bin/python3 src/app.py

clean:
	pyclean .
	rm -rf venv

test:
	PYTHONPATH=src ./venv/bin/python3 -m unittest discover -s ./test/model

venv/bin/activate: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt