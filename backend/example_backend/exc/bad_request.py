from typing import Dict

from flask import Response, jsonify


class BadRequest(Exception):
    status_code = 400

    def __init__(self, message: str, status_code: int = None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self) -> Dict:
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


def handle_bad_request(error: BadRequest) -> Response:
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
