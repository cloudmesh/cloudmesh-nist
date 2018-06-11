
mongo:
	docker run --name mongo -d -p 27017:27017 mongo --noauth --bind_ip=0.0.0.0
	docker ps

mongo_kill:
	docker stop mongo
	docker rm mongo

get_swagger:
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
