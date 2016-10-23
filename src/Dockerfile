FROM ubuntu:16.04
MAINTAINER Caner Dagli
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential git
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]

# docker build -t flask-api-starter .
# 
# For Development Container
# docker run -dt --name=flask-api-starter -v $PWD:/app -p 5000:5000 -e 'WORK_ENV=DEV' flask-api-starter
# 
# For Production Container
# docker run -dt --restart=always --name=flask-api-starter -p 5000:5000 -e 'WORK_ENV=PROD' flask-api-starter
# 
# Remove the container
# docker rm -f flask-api-starter

# docker logs --follow flask-api-starter
# docker exec -it flask-api-starter bash
