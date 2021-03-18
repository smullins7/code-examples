FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY example /app
RUN python3 init_db.py
RUN python3 migration-01.py

ENV FLASK_ENV=development
ENV FLASK_APP=main
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
ENTRYPOINT ["flask"]
CMD ["run"]
