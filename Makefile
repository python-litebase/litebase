install:
	pip install -e .

requirements:
	pip freeze --exclude-editable > requirements.txt
