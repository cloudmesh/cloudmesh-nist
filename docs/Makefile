.PHONY: spec

VERSION="Version 3.0.3"  
FILE=nistvol8-2

CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections --standalone
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--metadata link-citations=true --bibliography ./references.bib
CSS=--css=template/epub.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".."
#TITLE=--metadata title="NIST BDRA Volume 8"
LATEX=-N --template=./template.latex -V version=$(VERSION)
DEST=dest
SRC=../spec
MARKDOWN-OPTIONS=--verbose -V curdate="$(date)" --filter pandoc-codeblock-include --filter pandoc-crossref -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml

# --template=template.epub $(MERMAID) 

service_4= \
 alias\
 batchqueue\
 containers\
 database\
 default\
 deployment\
 file\
 filter\
 flavor\
 image\
 keyvaluestore\
 mapreduce\
 microservice\
 nic\
 organization\
 publickeystore\
 replica\
 reservation\
 scheduler\
 scheduler\
 secgroup\
 stream\
 timestamp\
 user\
 variables\
 virtualcluster\
 virtualdirectory\
 vm




# slurmjob\
# vcluster\


other=\
 abc\
 example\
 vm1


service=$(service_4)

broken= organization
#service=user keystore virtualdirectory virtualcluster


YAML := $(wildcard $(SRC)/*.yaml)

fast: dest rest spec cover epub
	open $(DEST)/$(FILE).epub

volume: dest rest spec epub html pdf word
	@echo "To open the document use:"
	@echo "open $(FILE).md"

cover:
	../bin/cover.py
	mkdir -p dest/images
	#cp template/cover-2-nist-formal.png dest/images
	#cp template/cover-nist-formal.png dest/images

dest: 
	mkdir -p $(DEST)/spec
	cp -r template dest
	cp -r images dest
	cp references.bib dest
	cp template.epub dest

#$(objects): dest/spec/%.md : ../services/%/%.yaml
#	../bin/cm-openapi2md md $< --indent=3 > $@

specstable:
	echo "Generate:" $(DEST)/spec/specstable.md ; \
	../bin/cm-specs-table "$(service)" > $(DEST)/specstable.md ; \


rest:
	for entry in $(service_4); do \
		echo "Generate:" $(DEST)/spec/$$entry.md ; \
		../bin/cm-openapi2md md $(SRC)/$$entry.yaml --indent=4 > $(DEST)/spec/$$entry.md ; \
		cp  $(SRC)/$$entry.yaml $(DEST)/spec; \
	done

lint:
	# find .. -name "*.yaml" -print0 | xargs -0 perl -pi.bak -e 's/ +$//'
	for entry in $(service); do \
		yamllint $(SRC)/$$entry/$$entry.yaml ; \
	done

setup:
	pip install -r ../requirements.txt

spec: dest cover specstable openapi $(FILE).md
#	cat dest/spec/*.md > dest/spec.md
	cat nistvol8-2.md status.md acronyms.md bib.md  > dest/$(FILE).md
	cd dest; ../../bin/cm-md-filter $(FILE).md > all.md
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT)  -s all.md -o $(FILE).md

epub: spec
	cp -rf images dest
	cd dest; pandoc --epub-cover-image=cover.png $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) --bibliography references.bib -o $(FILE).epub ../metadata.txt all.md
	cp $(DEST)/$(FILE).epub .

html: spec
	cp -rf images dest
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --toc -s $(FILE).md -o $(FILE).html
	cp $(DEST)/$(FILE).html .

pdf: spec  dest rest epub
	cp template.latex dest
	cp *.tex dest
	cp -rf images dest
#	cd dest; pandoc -H headers-include.tex $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) -V geometry:margin=1in -V fontsize=9pt --toc -s $(FILE).md -o $(FILE).pdf
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) $(LATEX) -V geometry:margin=1in -V fontsize=9pt --toc -s $(FILE).md -o $(FILE).pdf
	cp $(DEST)/$(FILE).pdf .
	open $(FILE).pdf .

tex: spec
	cp *.tex dest
	cp -rf images dest
#	cd dest; pandoc -H headers-include.tex $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) -V geometry:margin=1in -V fontsize=9pt --toc -s $(FILE).md -o $(FILE).tex
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) -V geometry:margin=1in -V fontsize=9pt --toc -s $(FILE).md -o $(FILE).tex
	cp $(DEST)/$(FILE).tex .

word: clean dest rest spec epub
	cp format.docx	$(DEST)
	# cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --reference-doc=format.docx -s $(FILE).md -o $(FILE).docx
	cd dest; pandoc $(TITLE) $(RESOURCE) $(MARKDOWN-OPTIONS) $(FORMAT) --bibliography references.bib --reference-doc=../../template/nist-bdra-template3.docx -s $(FILE).md -o $(FILE).docx
	cp $(DEST)/$(FILE).docx .


all:
	cd dest; pandoc $(RESOURCE) $(MARKDOWN-OPTIONS)  $(FORMAT) $(FONTS) $(BIB)  $(CSL) $(CSS) -o $(FILENAME).epub metadata.txt all.md


#pdf:
#        cd dest; pandoc -f markdown+smart --toc --epub-embed-font='fonts/*.ttf' -V geometry:margin=0.5in --bibliography references.bib --csl=../../template/ieee.csl# -o $(FILENAME).pdf metadata.txt $(INDEX)

clean:
	rm -rf dest

shell:
	docker run -v `pwd`:/book -w /book --rm -it cloudmesh/book:${VERSION}  /bin/bash 
