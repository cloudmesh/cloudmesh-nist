# SPECCY=docker run  -v $(PWD):/project  wework/speccy lint -v

define speccy_verify
	@echo "=================================================================="
	@echo $(1)
	@echo "=================================================================="
    speccy lint $(1)
endef

.PHONY: speccy

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

speccy:
	@echo "###################################################################"
	$(call speccy_verify,accounting.yaml)
	$(call speccy_verify,alias.yaml)
	$(call speccy_verify,batchqueue.yaml)
	$(call speccy_verify,containers.yaml)
	$(call speccy_verify,database.yaml)
	$(call speccy_verify,default.yaml)
	$(call speccy_verify,deployment.yaml)
	$(call speccy_verify,file.yaml)
	$(call speccy_verify,filter.yaml)
	$(call speccy_verify,flavor.yaml)
	$(call speccy_verify,group.yaml)
	$(call speccy_verify,image.yaml)
	$(call speccy_verify,keyvaluestore.yaml)
	$(call speccy_verify,mapreduce.yaml)
	$(call speccy_verify,microservice.yaml)
	$(call speccy_verify,nic.yaml)
	$(call speccy_verify,now.yaml)
	$(call speccy_verify,organization.yaml)
	$(call speccy_verify,publickeystore.yaml)
	$(call speccy_verify,replica.yaml)
	$(call speccy_verify,reservation.yaml)
	$(call speccy_verify,scheduler.yaml)
	$(call speccy_verify,secgroup.yaml)
	$(call speccy_verify,stream.yaml)
	$(call speccy_verify,user.yaml)
	$(call speccy_verify,variables.yaml)
	$(call speccy_verify,virtualcluster.yaml)
	$(call speccy_verify,virtualdirectory.yaml)
	$(call speccy_verify,vm.yaml)
	$(call speccy_verify,timestamp.yaml)
