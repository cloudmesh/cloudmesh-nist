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

#	redoc-cli bundle accounting.yaml
#	redoc-cli bundle batchqueue.yaml
#	redoc-cli bundle group.yaml
#	redoc-cli bundle mapreduce.yaml




html:
	mkdir -p ../docs/html
	redoc-cli bundle virtualcluster.yaml; mv redoc-static.html ../docs/html/virtualcluster.html
	redoc-cli bundle now.yaml; mv redoc-static.html ../docs/html/now.html
	redoc-cli bundle flavor.yaml; mv redoc-static.html ../docs/html/flavor.html
	redoc-cli bundle image.yaml; mv redoc-static.html ../docs/html/image.html
	redoc-cli bundle vm.yaml; mv redoc-static.html ../docs/html/vm.html
	redoc-cli bundle variables.yaml; mv redoc-static.html ../docs/html/variables.html
	redoc-cli bundle virtualdirectory.yaml; mv redoc-static.html ../docs/html/virtualdirectory.html
	redoc-cli bundle alias.yaml; mv redoc-static.html ../docs/html/alias.html
	redoc-cli bundle containers.yaml; mv redoc-static.html ../docs/html/containers.html
	redoc-cli bundle database.yaml; mv redoc-static.html ../docs/html/database.html
	redoc-cli bundle default.yaml; mv redoc-static.html ../docs/html/default.html
	redoc-cli bundle deployment.yaml; mv redoc-static.html ../docs/html/deployment.html
	redoc-cli bundle filestore.yaml; mv redoc-static.html ../docs/html/filestore.html
	redoc-cli bundle filter.yaml; mv redoc-static.html ../docs/html/filter.html
	redoc-cli bundle microservice.yaml; mv redoc-static.html ../docs/html/microservice.html
	redoc-cli bundle nic.yaml; mv redoc-static.html ../docs/html/nic.html
	redoc-cli bundle publickeystore.yaml; mv redoc-static.html ../docs/html/publickeystore.html
	redoc-cli bundle replica.yaml; mv redoc-static.html ../docs/html/replica.html
	redoc-cli bundle reservation.yaml; mv redoc-static.html ../docs/html/reservation.html
	redoc-cli bundle secgroup.yaml; mv redoc-static.html ../docs/html/secgroup.html
	redoc-cli bundle stream.yaml; mv redoc-static.html ../docs/html/stream.html
	redoc-cli bundle user.yaml; mv redoc-static.html ../docs/html/user.html
	redoc-cli bundle timestamp.yaml; mv redoc-static.html ../docs/html/timestamp.html
	redoc-cli bundle scheduler.yaml; mv redoc-static.html ../docs/html/scheduler.html
	redoc-cli bundle organization.yaml; mv redoc-static.html ../docs/html/organization.html
	cd ../docs/html; tree -H '.' -L 1 --noreport --charset utf-8 -P "*.zip" > index.html


speccy:
	@echo "###################################################################"
#	$(call speccy_verify,accounting.yaml)
	$(call speccy_verify,alias.yaml)
	$(call speccy_verify,containers.yaml)
	$(call speccy_verify,database.yaml)
	$(call speccy_verify,default.yaml)
	$(call speccy_verify,deployment.yaml)
	$(call speccy_verify,filestore.yaml)
	$(call speccy_verify,filter.yaml)
	$(call speccy_verify,flavor.yaml)
	$(call speccy_verify,image.yaml)
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
