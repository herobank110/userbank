# userbank

Users API in Python

# Usage

Install docker and run the following command:

```
docker-compose up -d --build
```

This will create three containers:
- `app_main`: the back end Python HTTP based API
- `app_test`: test for the back end API
- `db`: PostgreSQL database for data persistence

By default the API is served on port 3001. If needed this can can be
changed in the `docker/app_main.Dockerfile` CMD line, and updating the
`docker-compose.yml` ports option in `app_main`.

Once up and running you can explore the API using tools such as
Insomnia, and browse the [documentation](./docs/index.md) to learn
more.

## Testing

After the `app_test` is finished you can view its logs to see how the
tests went. The initial run of the container may result in test
failures as it depends on the live `db` container which may not have
started yet. Instead just restart the `app_test` container to rerun the
tests. This should also be done when the source code is changed.

