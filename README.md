# Flask Example

Example REST service using Flask. This repo is meant for demonstration/teaching purposes only. Production concerns like performance, scalability and security are absent from this project on purpose.

## Evolution to Target Architecture 

As a means of demonstrating how code evolves from an often overly simple implementation to a convoluted one, the following are the iterations of design and functionality for this project:

1. CRUD for blog posts
1. CRUD for comments on blog posts
1. CRUD for user accounts, blog posts and comments are no longer anonymous
1. tags for blog posts

As the functionality grows we want to address the following:

1. clear separation of concerns between classes
1. unit tests
1. using an ORM and database migration tool
1. logging and monitoring for observability

## Local Development

To run the entire stack simply do:
```shell
docker-compose up -d --build
```

This will start up the front end, back end and database. You can access the front end in your browser via [http://localhost:3000](localhost:3000)

If you want to curl the backend directly you can, e.g.
```shell
curl localhost:5000/posts
```


The app uses Docker for local development:

Build the app
```
docker build -t flask-example .
```

Run the app
```
docker run -d -p 5000:5000 flask-example
```

Then visit this URL in your browser: `http://localhost:5000`

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