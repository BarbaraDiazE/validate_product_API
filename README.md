## validate_product_api

### Install dependencies 
#### Create a virtual env
#### Install dependencies on requirements.txt
#### Install docker-compose. for more information, https://docs.docker.com/compose/install/
#### Activate virtual env

### To create database, run
```
docker-compose up
```
### Set up server
#### Migrations
```
python manage.py migrate
```
#### Start server
```
./run.sh
```
#### The servers run on:
```
0.0.0.0:8000
```
### Postman reports
Information avaliable at folder `/docs/`
