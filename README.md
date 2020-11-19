# IDM API 

RESTful microservise in flask framework 

### Pre-requirements

-add .env (reference in .env.template)

## API + MYSQLDB

# path/to/project/docker-compose build

# path/to/project/docker-compose up


### ENDPOINTS

```
POST /users
```
```
GET /users/distance/min
````
```
GET /users/distance/max
````
```
GET /logs/requests/{iso_code}/avg
````


### TESTS

```
export PYTHONPATH=$(pwd)
````
````
# pipenv install 
`````
```
# pipenv run coverage run --source app tests/__init__.py
`````
````
# pipenv run coverage report
````