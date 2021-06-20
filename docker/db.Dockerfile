FROM postgres:13-alpine
ENV POSTGRES_DB=Users
ENV POSTGRES_USER=docker
ENV POSTGRES_PASSWORD=hahaha123
COPY db/users_schema.sql /docker-entrypoint-initdb.d/users_schema.sql
