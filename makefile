install: venv
	. venv/bin/activate; pip3 install -Ur requirements.txt

venv:
	test -d venv || python3 -m venv venv

run:
	python ASD.py $(args)

clean:
	rm -rf venvfind -iname "*.pyc" -delete
