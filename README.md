# IDM API 

REST  microservice in Flask framework 

### Pre-requirements

-add .env (reference in .env.template)

## API

```
$ path/to/project/docker-compose build
````
```
$ path/to/project/docker-compose up
```

### ENDPOINTS

create new user:
```
POST /users
```
min distance from AR in km:
```
GET /users/distance/min
````
max distance from AR in km:
```
GET /users/distance/max
````
average of requests by country:
```
GET /logs/requests/{str:iso_code}/avg
````


## TESTS

set path
```
$ export PYTHONPATH=$(pwd)
````
install dependencies
````
$ pipenv install 
`````
run test
```
$ pipenv run coverage run --source app tests/__init__.py
`````
code coverage
````
$ pipenv run coverage report
````