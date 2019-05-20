.PHONY: test html-swagger html-spectable

OBJECTS=keystore profile vc

OBJECT=service
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


service: spec dest
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython2=true
	cp -rf ../services/conf.py ${DESTDIR}/swagger_server/
	cp -rf ../services/secconf.yaml ${DESTDIR}/swagger_server/
	@#cp -rf $(OBJECT)_controller.py $(DESTDIR)/swagger_server/controllers/default_controller.py
	cp -rf *controller.py $(DESTDIR)/swagger_server/controllers/
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

html-swagger:
	rm -rf html-swagger
	mkdir -p html-swagger
	@echo "------------------------------------------------------------------"
	cd html-swagger; swagger-codegen generate -i ../all.yaml -l html
	@echo "------------------------------------------------------------------"

html-swagger-dynamic:
	rm -rf html-swagger-dynamic
	mkdir -p html-swagger-dynamic
	@echo "------------------------------------------------------------------"
	cd html-swagger-dynamic; swagger-codegen generate -i ../all.yaml -l dynamic-html
	@echo "------------------------------------------------------------------"

html-spectable: json
	rm -rf html-spectable
	spectacle all.json
	mv -f public html-spectable

html-bootprint:
	# npm install -g bootprint
	# npm install -g bootprint-openapi
	bootprint openapi all.yaml htem-bootprint

html-redoc:
	# yarn add redoc
	# npm install redoc --save
	# npm install redoc-cli -g

view:
	open public/index.html

publish: service html-spectable
	cp -rf html-spectable/* ../../../docs/spec
	git add ../../../docs/spec
	git commit -m "update spec" ../../../docs
	git push

