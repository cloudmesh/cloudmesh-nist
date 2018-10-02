.PHONY: spec

FILE=nistvol8-2

MARKDOWN-OPTIONS=$(MERMAID) --filter pandoc-codeblock-include -f markdown+emoji -f markdown+header_attributes -f markdown+smart --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".."
TITLE=--metadata title="NIST BDRA Volume 8"
INCLUDE=--filter ~/.cabal/bin/pandoc-include-code 

DEST=dest/spec
SRC=../services


service=timestamp alias variables default file organization profile database replica virtualdirectory vc keystore vm scheduler


YAML := $(wildcard $(SRC)/*/*.yaml)

t:
	echo $(YAML)
	echo $(service)


volume: openapi

openapi: dest rest

dest: 
	mkdir -p $(DEST)


#$(objects): dest/spec/%.md : ../services/%/%.yaml
#	../bin/cm-openapi2md md $< --indent=3 > $@


rest:
	for entry in $(service); do \
		echo "Generate:" $(DEST)/$$entry.md ; \
		../bin/cm-openapi2md md $(SRC)/$$entry/$$entry.yaml --indent=3 > $(DEST)/$$entry.md ; \
	done



setup:
	pip install -r ../requirements.txt

text: rest
#	cat dest/spec/*.md > dest/spec.md
	cat nistvol8-2.md status.md acronyms.md bib.md > dest/$(FILE).md
	cd dest; ../../bin/cm-md-filter $(FILE).md > tmp.md
	cd dest; mv tmp.md $(FILE).md


html: text
	cp -rf images dest
	cd dest; pandoc $(INCLUDE) $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s $(FILE).md -o $(FILE).html

pdf: text
	cp -rf images dest
	cd dest; pandoc $(INCLUDE) $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s $(FILE).md -o $(FILE).pdf

word: text
	cd dest; pandoc $(INCLUDE) $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s $(FILE).md -o $(FILE).docx



all:
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md


pdf:
        cd dest; pandoc -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' -V geometry:margin=1in --bibliography references.bib --csl=../../template/ieee.csl -o $(FILENAME).pdf metadata.txt $(INDEX)

