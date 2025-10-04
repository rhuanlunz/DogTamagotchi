from flask import Blueprint, request, url_for, render_template, jsonify
from services.uuid_validation_service import validate_game_uuid_service
from services.menu_service import *

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/", methods=["GET"])
def render_menu():
    return render_template("menu.html")

@menu_blueprint.route("/create_new_game", methods=["GET"])
def create_new_game():
    valid_game_uuid = create_new_game_service()
    return jsonify({"redirect_url": url_for("game.render_game", save=valid_game_uuid)})

@menu_blueprint.route("/load_existing_game", methods=["GET"])
def load_existing_game():
    game_uuid = request.args.get("game")
    try:
        validate_game_uuid_service(game_uuid)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify({"redirect_url": url_for("game.render_game", save=game_uuid)})
