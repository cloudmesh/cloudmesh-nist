all:
	rm -f .spec.yaml
	cms openapi merge > /tmp/.spec.yaml
	mv /tmp/.spec.yaml .
	cms openapi codegen
	python server.py

