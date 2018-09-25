curl -H 'Content-Type: application/json' -H 'API-Key: alongstringtobeaapikey' -H 'API-Secret: anotherlongstringtobeaapisecret' -X PUT -d '{"name": "UbuntuFTP",  "host": "archive.ubuntu.com", "description": "Ubuntu FTP", "location": "/ubuntu/dists/bionic-updates/main/installer-amd64/current/images/netboot/", "protocal": "ftp", "credential": {"username": "anonymous", "password": "anonymous"}}' http://localhost:8080/cloudmesh/virtualdirectories
curl -u testuser:testsecret http://localhost:8080/cloudmesh/virtualdirectories

