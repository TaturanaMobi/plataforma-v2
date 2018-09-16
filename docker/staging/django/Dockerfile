FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev linux-headers \
  && apk add postgresql-dev \
  # Pillow dependencies
  # && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # CFFI dependencies
  # && apk add libffi-dev py-cffi \
  # Translations dependencies
  && apk add gettext \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client \
  && apk add uwsgi uwsgi-python3 nginx \
  # utils, like vim
  && apk add vim ansible bash

#RUN pip install uwsgi

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip3 install -r /requirements/staging.txt

COPY ./production/django/entrypoint /entrypoint
#RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./staging/django/start /start-django-app
#RUN sed -i 's/\r//' /start-django-app
RUN chmod +x /start-django-app

COPY ./staging/django/celery/worker/start /start-celeryworker
#RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./staging/django/celery/beat/start /start-celerybeat
#RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./staging/django/celery/flower/start /start-flower
#RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower

COPY ./staging/uwsgi.ini /uwsgi.ini
COPY ./staging/nginx.conf /etc/nginx/conf.d/default.conf
RUN mkdir -pv /run/nginx/
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN echo "/app" > /usr/local/lib/python3.6/site-packages/taturana.pth

#COPY ./taturana_key.pub /app/
#RUN echo $SECRETS_GIST
#RUN wget -O /app/.secrets ${SECRETS_GIST}
#RUN cat /app/.secrets
#RUN ansible-vault --vault-password-file /app/taturana_key.pub decrypt /app/.secrets
#RUN source /app/.secrets
#RUN echo ${SECRET_KEY}

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
