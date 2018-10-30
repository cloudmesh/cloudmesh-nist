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

DEST=dest
SRC=../services


service=timestamp alias variables default file profile database replica virtualdirectory virtualcluster keystore vm scheduler

broken= organization
#service=profile keystore virtualdirectory virtualcluster

YAML := $(wildcard $(SRC)/*/*.yaml)

fast: dest rest spec epub
	open $(DEST)/$(FILE).epub

volume: dest rest spec epub html pdf word
	@echo "To open the document use:"
	@echo "open $(FILE).md"

dest: 
	mkdir -p $(DEST)/spec


#$(objects): dest/spec/%.md : ../services/%/%.yaml
#	../bin/cm-openapi2md md $< --indent=3 > $@


rest:
	for entry in $(service); do \
		echo "Generate:" $(DEST)/spec/$$entry.md ; \
		../bin/cm-openapi2md md $(SRC)/$$entry/$$entry.yaml --indent=3 > $(DEST)/spec/$$entry.md ; \
		cp  $(SRC)/$$entry/$$entry.yaml $(DEST)/spec; \
	done

lint:
	# find .. -name "*.yaml" -print0 | xargs -0 perl -pi.bak -e 's/ +$//'
	for entry in $(service); do \
		yamllint $(SRC)/$$entry/$$entry.yaml ; \
	done

setup:
	pip install -r ../requirements.txt

spec: openapi dest/$(FILE).md
#	cat dest/spec/*.md > dest/spec.md
	cat nistvol8-2.md status.md acronyms.md bib.md > dest/$(FILE).md
	cd dest; ../../bin/cm-md-filter $(FILE).md > all.md
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s all.md -o $(FILE).md

epub: spec
	cp -rf images dest
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s all.md -o $(FILE).epub

html: spec
	cp -rf images dest
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s $(FILE).md -o $(FILE).html

pdf: spec
	cp -rf images dest
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --standalone -s $(FILE).md -o $(FILE).pdf

word: spec
	cp format.docx	$(DEST)
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --reference-doc=format.docx --standalone -s $(FILE).md -o $(FILE).docx


all:
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md


pdf:
        cd dest; pandoc -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' -V geometry:margin=1in --bibliography references.bib --csl=../../template/ieee.csl -o $(FILENAME).pdf metadata.txt $(INDEX)

clean:
	rm -rf dest
