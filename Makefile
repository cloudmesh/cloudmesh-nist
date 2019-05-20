OBJECTS=keystore profile virtualcluster virtualdirectory

.PHONY: service

doc:
	cd docs; make

word:
	cd docs; make word

view:
	open docs/dest/nistvol8-2.epub 

all: service controller
	@echo

service:
	bin/cm-openapi service generate $(OBJECTS) --target=service

controller:
	@#bin/cm-openapi controller generate $(OBJECTS) --target=service
	@echo $(OBJECTS)
	$(foreach svc, ${OBJECTS}, cp services/$(svc)/*controller.py service/;)

mongo-start:
	cd mongo; make -f Makefile mongo_start

mongo-kill:
	cd mongo; make -f Makefile mongo_kill

editor-install:
	docker pull swaggerapi/swagger-editor

editor-run:
	docker run -d -p 80:8080 swaggerapi/swagger-editor

clean:
	cd docs; make clean

volume:
	cd docs; make volume

CONTAINERS = $(shell docker ps -q -a)


kill:
	- $(shell docker kill $(CONTAINERS))
	- $(shell docker rm $(CONTAINERS))


demo-prepare: 
	cd mongo; make start
	make -f Makefile all

demo-service:
	osascript -e 'tell application "Terminal" to do script "cd $(PWD); cd service; make all"'
	sleep 10
	osascript -e 'tell application "Terminal" to do script "cd $(PWD); cd services/virtualdirectory/test; ./test_virtualdirectory.sh"'
	sleep 3
	@echo "==============================================================================="
	@echo "list the directories"
	@echo "==============================================================================="
	curl -u admin:secret http://localhost:8080/cloudmesh/virtualdirectories
	@echo "==============================================================================="
	@echo "list the UbuntuFTP directory"
	@echo "==============================================================================="
	curl -u admin:secret http://localhost:8080/cloudmesh/virtualdirectory/UbuntuFTP

demo: kill demo-prepare demo-service
	echo "done"
