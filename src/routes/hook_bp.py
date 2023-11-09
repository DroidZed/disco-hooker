from flask import request, json, abort, jsonify, Blueprint
from src.controllers.hook_controller import HookController
from src.models import ErrorResponse


bp = Blueprint("hook", __name__, url_prefix="/hook")


@bp.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@bp.post("/")
async def handle_hook():
    body = json.loads(request.data)
    result = await HookController().send_hook(body)

    match (result):
        case ErrorResponse():
            return abort(400, description=jsonify(result))

        case _:
            return jsonify({"message": "Ok"})
