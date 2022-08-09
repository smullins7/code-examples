# Code Examples

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

This repo is a hodge podge of coding examples primarily meant for teaching and mentoring. Nothing is meant to be taken as production level code, but rather examples are kept simple for easier demonstration and learning.

My skill set is definitely not UI so any frontend code in here will be very rough!

<p>
  <img width="450" height="300" src="https://media.giphy.com/media/3orieS4jfHJaKwkeli/giphy.gif" alt="simpsons example">
</p>

## Prerequisite

This repo uses [pre-commit hooks](https://github.com/pre-commit/pre-commit-hooks) for linting rules. It doesn't have great monorepo support so you'll want to just install it from this directory, then:

```shell
pre-commit install
```

With that done, any commits to any project within this repo will run the linter hooks before commiting.

## Blog Site

[blog-site](./blog-site/README.md) is a simple blogging site, with posts and comments.

### Frontend

The UI component of the blog site.

### Backend

The data as a service backend of the blog site.

![Python](https://img.shields.io/badge/python-3.8-blue.svg)
