from flask import Blueprint

game_blueprint = Blueprint("game", __name__)

@game_blueprint.route("/", methods=["GET"])
def render_game():
    return "render game"