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

verify:
	redoc-cli bundle accounting.yaml
	redoc-cli bundle alias.yaml
	redoc-cli bundle batchqueue.yaml
	redoc-cli bundle containers.yaml
	redoc-cli bundle database.yaml
	redoc-cli bundle default.yaml
	redoc-cli bundle deployment.yaml
	redoc-cli bundle file.yaml
	redoc-cli bundle filter.yaml
	redoc-cli bundle flavor.yaml
	redoc-cli bundle group.yaml
	redoc-cli bundle image.yaml
	redoc-cli bundle keyvaluestore.yaml
	redoc-cli bundle mapreduce.yaml
	redoc-cli bundle microservice.yaml
	redoc-cli bundle nic.yaml
	redoc-cli bundle now.yaml
	redoc-cli bundle organization.yaml
	redoc-cli bundle publickeystore.yaml
	redoc-cli bundle replica.yaml
	redoc-cli bundle reservation.yaml
	redoc-cli bundle scheduler.yaml
	redoc-cli bundle secgroup.yaml
	redoc-cli bundle stream.yaml
	redoc-cli bundle user.yaml
	redoc-cli bundle variables.yaml
	redoc-cli bundle virtualcluster.yaml
	redoc-cli bundle virtualdirectory.yaml
	redoc-cli bundle vm.yaml
	redoc-cli bundle timestamp.yaml

