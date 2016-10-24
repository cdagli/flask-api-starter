# flask-api-starter

[![Build Status](https://travis-ci.org/cdagli/flask-api-starter.svg?branch=master)](https://travis-ci.org/cdagli/flask-api-starter)

This project provides a boilerplate for building a Rest API using flask.

Other modules used are listed below; 
- sqlalchemy
- marshmallow
- sqlalchemy marshmallow
- flask sqlalchemy
- flask swagger

![alt text][screenshot]

[screenshot]: https://github.com/cdagli/flask-api-starter/blob/master/swagger.png
_*swagger documentation visualized with Swagger UI Console [Chrome extension](https://chrome.google.com/webstore/detail/swagger-ui-console/ljlmonadebogfjabhkppkoohjkjclfai)_

###To run locally:

```
git clone https://github.com/cdagli/flask-api-starter
cd flask-api-starter
virtualenv venv
source venv/bin/activate
cd src
pip install -r requirements.txt
python -m run 
```

Run tests:
```
nose2 -v
```

###Using Docker
Build with docker: 
```
git clone https://github.com/cdagli/flask-api-starter
cd flask-api-starter/src
docker build -t flask-api-starter .
```

Run in development mode: 
```
docker run -dt --name=flask-api-starter -v $PWD:/app -p 5000:5000 -e 'WORK_ENV=DEV' flask-api-starter
```

Run in production mode:
```
docker run -dt --restart=always --name=flask-api-starter -p 5000:5000 -e 'WORK_ENV=PROD' flask-api-starter
```

Remove the container:
```
docker rm -f flask-api-starter
```

To see logs and connect the container:
```
docker logs --follow flask-api-starter
docker exec -it flask-api-starter bash

```