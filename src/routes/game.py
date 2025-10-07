from flask import Blueprint, request, render_template
from domain.services.uuid_validation_service import validate_game_uuid_service

game_blueprint = Blueprint("game", __name__)

@game_blueprint.route("/gameplay", methods=["GET"])
def render_game():
    game_save = request.args.get("save")
    try:
        validate_game_uuid_service(game_save)
    except Exception as e:
        return str(e)

    return render_template("game.html")
