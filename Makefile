install:
	. venv/bin/activate; pip install -Ur requirements.txt

activate:
	. venv/bin/activate

install_venv:
	python3 -m venv venv
	. venv/bin/activate; python -m pip install --upgrade pip
	. venv/bin/activate; python -m pip install -r dev-requirements.txt

start:
	python3 -m venv venv
	. venv/bin/activate; python -m pip install --upgrade pip
	. venv/bin/activate; python -m pip install -r requirements.txt