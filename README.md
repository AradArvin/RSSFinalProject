# 🌟 RSS Final Project 🌟

Hello this is my final project for the makatab course. it host's a rss feed parser web application witch is written in django and django rest frame-work. the project is based upon diffrent technologies and It uses multilingual aspects as well.

> Reminder: this is a full back-end project so dont look forward to a pretty front.

## Programmer
### Alireza(Arad) Arvin  [GitHub Account](https://github.com/AradArvin)


## Technologies Used 

The technologies used by this app are mentioned below:

Programming language:

- [![Python][Python.js]][Python-url]

Frameworks: 

* [![Django][Django.js]][Django-url]
* [![Django Rest Framework][DRF.js]][DRF-url]

Third party appps:

- [![Github][Github.js]][Github-url]
- [![Docker][Docker.js]][Docker-url]
- [![Redis][Redis.js]][Redis-url]
- [![Celery][Celery.js]][Celery-url]
- [![Postgresql][Postgresql.js]][Postgresql-url]
- [![Rabbitmq][Rabbitmq.js]][Rabbitmq-url]
- [![Kibana][Kibana.js]][Kibana-url]
- [![Elasticsearch][Elasticsearch.js]][Elasticsearch-url]


## Starting Notes

This app is using the docker technology, so the app settings are configured to run on docker. please follow the installation guide carefully.



## Installation Guide

Since this project uses the django project technology I recommend you to read this part to properly set up the project.

- 1. first: It's better to fork this project to your own repo.(of course you can skip this step...)

- [![Fork][Fork.js]][Fork-url]

- 2. clone the forked repo to you'r local repository >>>
    
```bash
git clone https://github.com/AradArvin/RSSFinalProject.git
```

- 3. make a virtual environment for the django project(you should use a venv. It's recommended) >>>
    
```bash
python3 -m venv .venv
```

- 4. activate the venv >>>

```bash
source .venv/bin/activate
```

- 5. now you need to dockerize the project >>>

```bash
docker compose -f "docker-compose.yml" up -d --build
```
> This command first creates the docker containers and then upstreams the app so that it could run.  


#### Now you are ready to inspect the project and enjoy It's aspects. All you need to do now is to enter http://127.0.0.1:8000/ in your browser and navigate the urls in the app.


- In order to stop the docker and exit the project:

```bash
docker compose -f "docker-compose.yml" down
```
> make sure that docker is installed on you'r computer


## Docker Compose

There are a few things you must consider when dockerizing:

1. the docker containers are built using the **docker-compose.yml** file. in fact this file is responsible for the whole dockerizing process. so make sure that you are in the directory of this file then docker build up.

2. since docker use a great amount of you'r hardware, make sure you'r pc is capable of running a big number of containers.

3. the database is using a virtual environment variable or .env file so you need to enter your own config in order to run this app.

the configs you need to involve in the .env file are:

- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT

> keep in mind that the database used in this project is postgresql.




[Python.js]: https://img.shields.io/badge/Python-yellow?style=for-the-badge&logo=python&logoColor=black
[Python-url]: https://www.python.org/


[Django.js]: https://img.shields.io/badge/Django-green?style=for-the-badge&logo=django&logoColor=black
[Django-url]: https://www.djangoproject.com/


[DRF.js]: https://img.shields.io/badge/Django%20Rest%20Framework-red?style=for-the-badge
[DRF-url]: https://www.django-rest-framework.org/


[Github.js]: https://img.shields.io/badge/GitHub-green?style=for-the-badge&logo=github&logoColor=black
[Github-url]: https://github.com/


[Docker.js]: https://img.shields.io/badge/docker-blue?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://docker.com/


[Rabbitmq.js]: https://img.shields.io/badge/rabbitmq-white?style=for-the-badge&logo=rabbitmq&logoColor=orange
[Rabbitmq-url]: https://rabbitmq.com/


[Elasticsearch.js]: https://img.shields.io/badge/elasticsearch-white?style=for-the-badge&logo=elasticsearch&logoColor=blue
[Elasticsearch-url]: https://www.elastic.co/elasticsearch/


[Kibana.js]: https://img.shields.io/badge/kibana-white?style=for-the-badge&logo=kibana&logoColor=green
[Kibana-url]: https://www.elastic.co/kibana


[Postgresql.js]: https://img.shields.io/badge/postgresql-blue?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org/


[Redis.js]: https://img.shields.io/badge/redis-red?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/


[Celery.js]: https://img.shields.io/badge/celery-white?style=for-the-badge&logo=celery&logoColor=green
[Celery-url]: https://docs.celeryq.dev/en/stable/


[Fork.js]: https://img.shields.io/badge/fork-green?style=for-the-badge&logo=github&logoColor=black
[Fork-url]: https://docs.github.com/en/get-started/quickstart/fork-a-repo