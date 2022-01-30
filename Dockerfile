FROM apache/airflow:2.2.3

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir git+https://github.com/takuti-sandbox/airflow-test.git#egg=takuti\&subdirectory=pkg
ENV AIRFLOW__LINEAGE__BACKEND=takuti.lineage.ExampleBackend
