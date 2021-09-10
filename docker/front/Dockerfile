FROM node:14.16.0-stretch-slim

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN yarn global add @vue/cli @vue/cli-init

COPY ./docker/front/docker-entrypoint.sh docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh

WORKDIR /app