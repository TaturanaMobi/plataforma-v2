FROM postgres:10.5
COPY ./production/postgres/maintenance /usr/local/bin/maintenance
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
RUN mkdir -pv /docker-entrypoint-initdb.d
COPY ./dev/sentry/create-sentry.sh /docker-entrypoint-initdb.d/
