# ApiStorageContent
RESTful API to list content of a filesystem/directory on OS supporting Python3 language

Build (docker):
docker-compose build
docker-compose run --rm api flask db upgrade
docker-compose up api
curl -u admin:secret localhost:8080/v1/users | python -m json.tool

Sources:
https://medium.com/python-rest-api-toolkit/build-a-python-rest-api-in-5-minutes-c183c00d3465
