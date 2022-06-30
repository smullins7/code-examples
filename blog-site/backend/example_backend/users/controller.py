from flask import Blueprint, jsonify

from example_backend.users.service import auth_required

blueprint = Blueprint("user", __name__, url_prefix="/users")


@blueprint.route("", methods=("POST",))
@auth_required(inject_user=True, inject_id_info=True)
def create_or_verify_user(user, id_info):
    return jsonify({"user": user.to_dict(), "id_info": id_info})
