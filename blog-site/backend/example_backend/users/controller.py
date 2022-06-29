from flask import jsonify

from example_backend.app import app
from example_backend.exc.bad_request import BadRequest
from example_backend.users.service import resolve_user


@app.route("/users", methods=("POST",))
def create_or_verify_user():
    try:
        user, id_info = resolve_user()
        return jsonify({"user": user.to_dict(), "id_info": id_info})
    except ValueError as e:
        raise BadRequest(str(e))
