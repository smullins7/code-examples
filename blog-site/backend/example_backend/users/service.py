import re
from typing import Dict

import flask
from google.auth.transport import requests
from google.oauth2 import id_token

from example_backend.exc.bad_request import BadRequest
from example_backend.users import dao
from example_backend.users.dao import User

AUTH_HEADER_PAT = re.compile(r"^Bearer (?P<token>.*)$")
CLIENT_ID = "362134854545-t9ni0g6vtl1igvv2gmk8ehjk5tr315p4.apps.googleusercontent.com"


def verify_token(token: str) -> Dict:
    request = requests.Request()
    return id_token.verify_oauth2_token(token, request, CLIENT_ID)


def _resolve_user(token: str) -> tuple[User, Dict]:
    id_info = verify_token(token)
    user = dao.find_by_email(id_info["email"])
    if not user:
        user = dao.insert(id_info["email"], id_info["name"])
    return user, id_info


def resolve_user() -> tuple[User, Dict]:
    if "Authorization" not in flask.request.headers:
        raise BadRequest("Authorization header required")

    auth_header = flask.request.headers["Authorization"]
    m = AUTH_HEADER_PAT.match(auth_header)
    if not m:
        raise BadRequest("Authorization header malformed, value must be 'Bearer <jwt token>")

    return _resolve_user(m.group("token"))
