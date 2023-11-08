from flask import request, Flask, json, abort, jsonify
from src.config.env import Env

from src import DiscordWebHookManager

Env()

app = Flask(__name__)


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


@app.get("/")
async def index():
    return "OK."


@app.post("/hook")
async def handle_hook():
    body = json.loads(request.data)

    result = await DiscordWebHookManager().notify_channel(
        title=body["title"],
        message=body["msg"],
        color=body["status"],
        fields=body["jobs"],
    )

    if result is None:
        return jsonify({"message": "Ok"})

    if result.status_code != 200:
        abort(
            400,
            description=json.loads(
                result.content.decode("utf-8")
            ),
        )

    return jsonify({"message": "Ok"})


@app.put("/rehook")
async def update_hook_embed():
    body = json.loads(request.data)
    title = request.args.get("title", "", type=str)
    result = await DiscordWebHookManager().update_channel(
        for_title=title, with_fields=body["new_jobs"]
    )
    return jsonify(result)
