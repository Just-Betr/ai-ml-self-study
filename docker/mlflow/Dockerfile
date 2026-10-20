FROM ghcr.io/mlflow/mlflow:v3.17.1
# The official image has no Postgres driver.
RUN pip install --no-cache-dir "psycopg[binary]>=3.2,<4"
