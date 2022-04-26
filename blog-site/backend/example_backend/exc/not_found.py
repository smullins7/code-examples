from typing import Dict

from flask import Response, jsonify


class NotFound(Exception):
    status_code = 404

    def __init__(self, message: str):
        Exception.__init__(self)
        self.message = message

    def to_dict(self) -> Dict:
        return {"message": self.message}


def handle_not_found(error: NotFound) -> Response:
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
