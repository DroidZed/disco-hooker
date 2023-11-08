from flask import request, json, abort, jsonify, Blueprint
from src.controllers.hook_controller import HookController
from src.models import WebhookResponse


bp = Blueprint("hook", __name__, url_prefix="/hook")


@bp.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@bp.post("/")
async def handle_hook():
    body = json.loads(request.data)
    result = await HookController().send_hook(body)

    match (result):
        case str():
            return abort(400, description=jsonify(result))

        case WebhookResponse():
            return jsonify(result)

        case _:
            return abort(
                400, description=jsonify({"error": "None"})
            )


@bp.put("/")
async def update_hook_embed():
    body = json.loads(request.data)

    title = request.args.get("title", "", type=str)
    wh_id = request.args.get("id", "", str)

    result = await HookController().update_embed(
        title, wh_id, body
    )

    print(result)

    match (result):
        case str():
            return abort(400, description=result)

        case WebhookResponse():
            return jsonify(result)

        case _:
            return abort(
                400, description=jsonify({"error": "None"})
            )
