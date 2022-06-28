# Blog Site

This is a dummy blog site, with a frontend, backend and database.

<p>
  <img width="330" height="335" src="https://imgs.xkcd.com/comics/blogging.png" alt="blogging">
</p>

Things this project _does not_ care about:
 - performance/scaling
 - security
 - UI

Things this project _does_ demonstrate:
 - poetry
 - Flask
 - Docker
 - Make
 - MySQL DB/migrations
 - separation of concerns
 - unit tests
 - coding style/checks

## Setup

This project requires Docker, NPM and Python. It also requires a `.env` file for `docker-compose` to work. To generate a `.env` in this directory do:

```shell
echo "MYSQL_HOST_PORT=3306" > .env
```

If you need to run the database on a different port you can just change the `.env` file contents, and check them with `docker-compose config`.

# TODO

0.5. database snapshot
1. Add user login
2. add audit/history
3. add tags to posts by author
