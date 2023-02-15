# python version variable
ARG PYTHON_VERSION=3.9-slim-bullseye

#python version to be used
FROM python:${PYTHON_VERSION} as python
# python build stage
FROM python as python-build-stage
# environment variable
ARG BUILD_ENVIRONMENT=local

# install python dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev 

# copy requirements 
COPY ./requirements .

# install requirements from the environment variables   
RUN pip wheel --wheel-dir /usr/src/app/wheels \
   -r ${BUILD_ENVIRONMENT}.txt

# python run stage
FROM python as python-run-stage

ARG BUILD_ENVIRONMENT=local
# app directory
ARG APP_HOME=/app

# environment variables
# prevent python to write .pyc files to disk
ENV PYTHONDOTWRITEBYTECODE 1
# python output is directly transmitted to the terminal
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# install system dependencies 
RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# copy python dependencies to wheels
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
   && rm -rf /wheels/

# script to run 
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY ./docker/local/django/celery/worker/start /start_celeryworker
RUN sed -i 's/\r$//g' /start_celeryworker
RUN chmod +x /start_celeryworker

COPY ./docker/local/django/celery/flower/start /start_flower
RUN sed -i 's/\r$//g' /start_flower
RUN chmod +x /start_flower

# copy to working directory
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]


