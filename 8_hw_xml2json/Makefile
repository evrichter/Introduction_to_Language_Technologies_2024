ORIGINAL_TSV_FILE = dependency_trees_from_ud.tsv
FILE_NAME_XML = sample.xml
FILE_NAME_JSON = sample.json
FILE_NAME_TSV = sample.tsv


download:
	@wget -O dependency_trees_from_ud.tsv https://ufal.mff.cuni.cz/~zabokrtsky/courses/npfl125/data/dependency_trees_from_ud.tsv

tsv2xml:
	python3 conversion_tools.py tsv2xml $(ORIGINAL_TSV_FILE)

xml2json:
	python3 conversion_tools.py xml2json $(FILE_NAME_XML)

json2tsv:
	python3 conversion_tools.py json2tsv $(FILE_NAME_JSON)

check:
	python3 conversion_tools.py check $(ORIGINAL_TSV_FILE)

report:
	python3 conversion_tools.py report

all: download tsv2xml xml2json json2tsv check report