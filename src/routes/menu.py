from flask import Blueprint, request, url_for, redirect, render_template, jsonify
from infrastructure.database import create_game, is_game_exist
from uuid import uuid4, UUID

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/", methods=["GET"])
def render_menu():
    return render_template("menu.html")

@menu_blueprint.route("/create_new_game", methods=["GET"])
def create_new_game():
    game_uuid_str = str(uuid4())
    create_game(game_uuid_str)
    return redirect(url_for("game.render_game", save=game_uuid_str))

@menu_blueprint.route("/load_existing_game", methods=["GET"])
def load_existing_game():
    game_uuid = request.args.get("game")
    if game_uuid is None:
        return jsonify({"error": "Game URL Parameter is none."}), 400
    
    try:
        UUID(game_uuid)
    except ValueError:
        return jsonify({"error": "Invalid game UUID or game does not exist."}), 400
    
    if not is_game_exist(game_uuid):
        return jsonify({"error": "Invalid game UUID or game does not exist."}), 400

    return jsonify({"redirect_url": url_for("game.render_game", save=game_uuid)})
