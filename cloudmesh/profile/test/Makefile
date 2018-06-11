
start:
	docker run --name mongo -d -p 27017:27017 mongo --noauth --bind_ip=0.0.0.0
	docker ps

kill:
	docker stop mongo
	docker rm mongo

