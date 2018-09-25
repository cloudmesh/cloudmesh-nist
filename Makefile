OBJECTS=keystore profile vc virtualdirectory

.PHONY: service

all: service controller
	@echo

service:
	bin/cm-openapi service generate $(OBJECTS) --target=service

controller:
	@#bin/cm-openapi controller generate $(OBJECTS) --target=service
	@echo $(OBJECTS)
	$(foreach svc, ${OBJECTS}, \
		cp services/$(svc)/*controller.py service/;)

mongo-start:
	make -f Makefile mongo_start

mongo-kill:
	make -f Makefile mongo_kill

editor-install:
	docker pull swaggerapi/swagger-editor

editor-run:
	docker run -d -p 80:8080 swaggerapi/swagger-editor
