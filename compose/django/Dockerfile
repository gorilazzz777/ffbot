FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /src
RUN mkdir -p /var/log/app
RUN mkdir /static
RUN chmod -R 777 /static
RUN chmod -R 777 /var/log/app

WORKDIR /src

RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg

RUN apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev 

RUN pip install --upgrade pip

COPY ./src/requirements.pip /scripts/
RUN pip install --no-cache-dir -r /scripts/requirements.pip

RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

CMD ["sh", "-c", "python manage.py collectstatic --no-input; python manage.py migrate; python manage.py loaddata start_data; gunicorn app.wsgi -b 0.0.0.0:8000"]
