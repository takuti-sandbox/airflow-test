Testing Apache Airflow
===

## Setup

[Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html):

```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.3/docker-compose.yaml'
```

Comment `image:` and uncomment `build: .`, so that the containers are created based on an extended [`Dockerfile`](./Dockerfile):

```yml
version: '3'
x-airflow-common:
  &airflow-common
  # In order to add custom dependencies or upgrade provider packages you can use your extended image.
  # Comment the image line, place your Dockerfile in the directory where you placed the docker-compose.yaml
  # and uncomment the "build" line below, Then run `docker-compose build` to build the images.
  # image: ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.2.3}
  build: .
  environment:
    &airflow-common-env
    ...
```

## Usage

Edit `dags/` and `plugins/`, which are mounted to the containers.

```sh
docker-compose down --volumes --remove-orphans \
    && docker-compose build --no-cache \
    && docker-compose up
```

http://localhost:8080/ (Username: `airflow`, Password: `airflow`)

## References

- [What is Data Lineage](https://www.trifacta.com/data-lineage/)
- [Extending the original Airflow image](https://airflow.apache.org/docs/docker-stack/build.html)