from flask import Blueprint, request, url_for, render_template, jsonify
from services.menu_service import *
from services.uuid_validation_service import is_valid_uuid

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/", methods=["GET"])
def render_menu():
    return render_template("menu.html")

@menu_blueprint.route("/create_new_game", methods=["GET"])
def create_new_game():
    valid_game_uuid = create_new_game_service()
    return valid_game_uuid

@menu_blueprint.route("/load_existing_game", methods=["GET"])
def load_existing_game():
    game_uuid = request.args.get("game")
    
    if not is_valid_uuid(game_uuid):
        return jsonify({"error": "Invalid game UUID or game does not exist."}), 400

    return jsonify({"redirect_url": url_for("game.render_game", save=game_uuid)})
