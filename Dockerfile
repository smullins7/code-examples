FROM python:3.9

WORKDIR /app

RUN pip install poetry==1.1.5

COPY pyproject.toml poetry.lock /app/

# use poetry to emit the dependencies but use pip to install without a virtualenv
# doing this because Docker is already a contained environment so virtualenv seems unnecessary
RUN poetry export --without-hashes -f requirements.txt | pip install -r /dev/stdin

COPY example /app
RUN python3 init_db.py
RUN python3 migration-01.py

ENV FLASK_ENV=development
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run"]