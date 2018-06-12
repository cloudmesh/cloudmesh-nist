.PHONY: test

OBJECTS=keystore profile

OBJECT=all
CLOUDMESH=..
SWAGGERCODEGEN=java -jar $(CLOUDMESH)/bin/swagger-codegen-cli-2.3.1.jar
YAMLFILE=$(OBJECT).yaml
DESTDIR=server/$(OBJECT)/flaskConnexion
CREATED=server

all: spec service start
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

spec:
	cd ..; make -f Makefile service


s: 

service: spec dest
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython2=true
	cp -rf $(OBJECT)_controller.py $(DESTDIR)/swagger_server/controllers/default_controller.py
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install

start:
	pip install pymongo
	cd $(DESTDIR) && python -m swagger_server

test:
	sh ../services/keystore/test/test_keystore.sh
	sh ../services/profile/test/test_profile.sh

stop:
	ps | grep swagger | grep -v "grep"| awk '{print $$1}' | xargs kill -9

clean:
	rm -rf $(CREATED)
	rm -rf public

container:
	docker build -t cloudmesh-$(OBJECT) .
	docker run -p 8080:8080 cloudmesh-$(OBJECT)

json:
	@echo "------------------------------------------------------------------"
	swagger-codegen generate -i all.yaml -l swagger
	@echo "------------------------------------------------------------------"
	mv swagger.json all.json

doc: json
	spectacle all.json

view:
	open public/index.html

publish: service doc
	cp -rf public/* ../../../docs/spec
	git add ../../../docs/spec
	git commit -m "update spec" ../../../docs
	git push

