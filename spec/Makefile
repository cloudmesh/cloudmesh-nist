SPECCY=docker run  -v $(PWD):/project  wework/speccy lint -v

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
