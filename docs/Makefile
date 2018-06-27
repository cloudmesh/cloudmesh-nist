.PHONY: spec

FILE=nistvol8-2



MARKDOWN-OPTIONS=$(MERMAID) -f markdown+header_attributes -f markdown+smart -f markdown+emoji --indented-code-classes=bash,python,yaml
CSL=--csl=template/ieee-with-url.csl
FORMAT=--toc --number-sections
FONTS=--epub-embed-font='fonts/*.ttf'
BIB=--bibliography references.bib
CSS=--css=template/epub.css
CSS_HTML=--css=template/pandoc.css
RESOURCE=--resource-path=".."
TITLE=--metadata title="NIST BDRA Volume 8"
INCLUDE=--filter ~/.cabal/bin/pandoc-include-code 

#spec:
#	cp ../services/vc/vc.yaml 

md:
	# ls -1 ../services/*/*.yaml > yaml.txt
	../bin/cm-openapi2md md ../services/alias/alias.yaml --indent=3 > spec/alias.md
	../bin/cm-openapi2md md ../services/database/database.yaml  --indent=3 > spec/database.md
	../bin/cm-openapi2md md ../services/default/default.yaml  --indent=3 > spec/default.md
	../bin/cm-openapi2md md ../services/file/file.yaml  --indent=3 > spec/file.md
	../bin/cm-openapi2md md ../services/organization/organization.yaml  --indent=3 > spec/organization.md
	../bin/cm-openapi2md md ../services/profile/profile.yaml  --indent=3 > spec/profile.md
	../bin/cm-openapi2md md ../services/replica/replica.yaml  --indent=3 > spec/replica.md
	../bin/cm-openapi2md md ../services/variables/variables.yaml  --indent=3 > spec/variables.md
	../bin/cm-openapi2md md ../services/virtualdirectory/virtualdirectory.yaml  --indent=3 > spec/virtualdirectory.md
	../bin/cm-openapi2md md ../services/timestamp/timestamp.yaml > spec/timestamp.md
	../bin/cm-openapi2md md ../services/vc/vc.yaml > spec/vc.md
	../bin/cm-openapi2md md ../services/keystore/keystore.yaml > spec/keystore.md
	../bin/cm-openapi2md md ../services/vm/vm.yaml > spec/vm.md
	../bin/cm-openapi2md md ../services/scheduler/scheduler.yaml > spec/scheduler.md

	echo >  spec/user.md
#	../bin/cm-openapi2md md ../services/user/user.yaml > spec/user.md

text: md
#	cat spec/*.md > dest/spec.md
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

