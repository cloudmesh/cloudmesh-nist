include ../make.mk

# SPECCY=docker run  -v $(PWD):/project  wework/speccy lint -v

define speccy_verify
	@echo "=================================================================="
	@echo $(1)
	@echo "=================================================================="
    speccy lint $(1)
endef

.PHONY: speccy html

all:
	rm -f .spec.yaml
	cms openapi merge > /tmp/.spec.yaml
	mv /tmp/.spec.yaml .
	cms openapi codegen
	python server.py



lint:
	$(SPECCY) file.yaml


install:
	npm install -g swagger-cli


#	redoc-cli bundle non.yaml
html:
	mkdir -p ../docs/html
	for entry in $(resources); do \
		echo "############################" ; \
		echo "#" $$entry; \
		echo "############################" ; \
		redoc-cli bundle $$entry.yaml; mv redoc-static.html ../docs/html/$$entry.html ; \
	done
	cd ../docs/html; tree -H '.' -L 1 --noreport --charset utf-8 -P "*.html" >	index.html

# speccy lint non.yaml
speccy:
	mkdir -p ../docs/html
	for entry in $(resources); do \
		echo "############################" ; \
		echo "#" $$entry; \
		echo "############################" ; \
		speccy lint $$entry.yaml ; \
	done
	cd ../docs/html; tree -H '.' -L 1 --noreport --charset utf-8 -P "*.html" >	index.html

