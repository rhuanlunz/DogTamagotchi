from flask import Blueprint, request
from infrastructure.database import is_game_exist

game_blueprint = Blueprint("game", __name__)

@game_blueprint.route("/gameplay", methods=["GET"])
def render_game():
    game_save = request.args.get("save")
    if game_save is None:
        return "Save parameter is none", 400

    if not is_game_exist(game_save):
        return "Inexistent game", 404

    return "render game"