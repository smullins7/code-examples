# TODO

1. add audit/history
2. add users to backend
3. add abstraction to backend
4. frontend for all functionality on backend
5. make a decent effort on frontend style
6. logging/monitoring to backend?
7. add tags to posts by author?

# Backend REST Example

Example REST service using Flask. This repo is meant for demonstration/teaching purposes only. Production concerns like performance, scalability and security are absent from this project on purpose.

## Local Development

### Docker

To run the entire stack simply do the following from the _parent_ directory:
```shell
docker-compose up -d --build
```

This will start up the front end, back end and database. You can access the front end in your browser via [http://localhost:3000](localhost:3000)

If you want to curl the backend directly you can, e.g.
```shell
curl localhost:4000/posts
```

If you want to access the database directly you can (assuming you have the client installed), e.g.
```shell
mysql -uexampleuser -pdev -h 127.0.0.1 -P 3306 example
```

The app uses Docker for local development:

Build the app
```
docker build -t flask-example .
```

Run the app
```
docker run -d -p 4000:4000 flask-example
```

Then visit this URL in your browser: `http://localhost:4000`

### Non-Docker

Ensure the poetry environment has the latest dependencies installed:

```
poetry install
```

Either run a mysql server on your machine or via Docker (e.g. `docker-compose -d up database` in the _parent_ directory). Then use make to start the service:

```
make start
```

### DB Migrations

Whenever making changes to the models run this command once the changes are in place:
```
flask db migrate -m "Your message here"
```

This will produce a migration script like:
```
example/migrations/versions/177e5febe83c_.py
```

You can verify the script looks correct. When the application starts up, database migrations will run automatically to apply those changes.
