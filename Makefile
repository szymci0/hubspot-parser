base_install:
	@pip install -r requirements.txt

base_run:
	@python hubspot_parser.py

help:
	@python hubspot_parser.py -h

unit_tests:
	@python hubspot_parser.py -t
