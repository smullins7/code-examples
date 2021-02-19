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

To run the app locally do the following:

1. install the dependencies
1. setup the database
1. configure flask
1. start the app

### Install the dependencies

You may choose to use a `virtualenv` to contain the environment for this project, if not skip this part. To install `virtualenv`:

```shell
pip3 install virtualenv
```

Then in the directory of your choice (such as `~/envs`):

```shell
virtualenv -p python3 flask-example
source flask-example/bin/activate
```

Now install the dependencies from the root directory of this project:

```shell
pip3 install -r requirements.txt
```

### Setup the database

Run these command from the `example` directory:

```shell
python3 init_db.py
python3 migration-01.py
```

### Configure Flask

```shell
export FLASK_ENV=development
export FLASK_APP=main
```

### Star the app

Run this command from the `example` directory:

```shell
flask run
```