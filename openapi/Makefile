OBJECTS=keystore profile

.PHONY: service

service: openapi controller
	@echo

openapi:
	bin/merge-openapi.py $(OBJECTS) --out service/all.yaml

controller:
	bin/cat_controllers.py keystore profile > service/all_controller.py

mongo-start:
	make -f Makefile mongo_start


mongo-kill:
	make -f Makefile mongo_kill

editor-install:
	docker pull swaggerapi/swagger-editor

editor-run:
	docker run -d -p 80:8080 swaggerapi/swagger-editor
