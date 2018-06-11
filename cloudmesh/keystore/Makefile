.PHONY: test

SWAGGERCODEGEN=java -jar ../core/swagger/swagger-codegen-cli-2.3.1.jar
YAMLFILE=profile.yaml
DESTDIR=server/profile/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

service: dest
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython2=true
	cp -r *.py $(DESTDIR)/swagger_server/controllers/default_controller.py
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 

start:  
	pip install pymongo
	cd $(DESTDIR) && python -m swagger_server

test:
	sh test/test_profile.sh

stop:
	ps | grep swagger | grep -v "grep"| awk '{print $$1}' | xargs kill -9

clean:
	rm -rf $(CREATED)

container:
	docker build -t cloudmesh-profile .
	docker run -p 8080:8080 cloudmesh-profile


