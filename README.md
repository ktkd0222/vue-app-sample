# Vue + Fast API sample web application
sample web application

# Requirement
- Docker 20.10.8
- docker-compose 1.29.2

# Docker build and launch
```bash
$ git clone https://github.com/ktkd0222/vue-app-sample.git
$ cd vue-app-sample
$ sudo docker-compose build
$ sudo docker-compose up -d
```

# Default port each containers
| container | port |
| -- | -- |
| front | 80 |
| back | 3000 |


You may need to set up port forward.

# Development
Please comment out `command ./docker-entrypoint.sh` in docker-compose.yml

## launch front server for development
```bash
$ sudo docker-compose exec front bash
$ yarn install
$ yarn serve
```

## launch back server for development
```bash
$ sudo docker-compose exec back bash
$ uvicorn server:app --host 0.0.0.0 --port 3000 --reload
```