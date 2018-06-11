.PHONY: test

SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=profile.yaml
DESTDIR=server/profile/flaskConnexion
CREATED=server

all: service start 
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

service: dest
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython2=true

	cp -r *.py $(DESTDIR)/swagger_server/controllers
	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 

start:  
	pip install pymongo
	cd $(DESTDIR) && python -m swagger_server

test:
	curl -H 'Content-Type: application/json' -X PUT -d '{"usename": "testname", "firstname": "John", "lastname": "Doe", "publickey": "ssh-rsa:xxx", "email": "user@exmaple.com"}' http://localhost:8080/cloudmesh/profile/profiles
	curl http://localhost:8080/cloudmesh/profile/profiles/135
	curl http://localhost:8080/cloudmesh/profile/profiles

stop:
	ps | grep swagger | grep -v "grep"| awk '{print $$1}' | xargs kill -9

clean:
	rm -rf $(CREATED)
	rm *.jar

container:
	docker build -t cloudmesh-profile .
	docker run -p 8080:8080 cloudmesh-profile

mongo:
	docker run --name mongo -d -p 27017:27017 mongo --noauth --bind_ip=0.0.0.0
	docker ps

mongo_kill:
	docker stop mongo
	docker rm mongo

get_swagger:
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
