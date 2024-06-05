# FastAPI Workspace Dockerized

Trying to dev FastAPI in docker container.

## Development with Docker

Run the app container:

```shell
docker compose up -d
```

Example endpoint will available on `localhost:8000`.

Now open `app/main.py`, uncomment a section to see hot reload is working.

## Building Docker Image

For production usually with build the image and not using docker compose.

```shell
docker build image build -t fastapi:latest .
```

Now run the docker image, pretending on production behavior.

```shell
docker container run -d -p=8001:8000 fastapi:latest
```

It's gonna using 8001 port on host. Now open `localhost:8001`.

To stop the a running container of it, first find the id of it.

```shell
docker container ps
      STATUS              PORTS                    NAMES
e06472c24073   fastapi:latest   "make start"   About a minute ago   Up About a minute   0.0.0.0:8001->8000/tcp   eloquent_moser

docker container kill e06472c24073
```
