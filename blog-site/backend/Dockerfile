FROM python:3.9

WORKDIR /app

RUN pip install poetry==1.1.5

COPY entrypoint.sh pyproject.toml poetry.lock /app/
COPY migrations /app/migrations

# use poetry to emit the dependencies but use pip to install without a virtualenv
# doing this because Docker is already a contained environment so virtualenv seems unnecessary
RUN poetry export --without-hashes -f requirements.txt | pip install -r /dev/stdin

COPY example_backend/ /app/example_backend

ENV FLASK_ENV=development
ENV FLASK_APP=example_backend.app
EXPOSE 4000

RUN chmod u+x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
