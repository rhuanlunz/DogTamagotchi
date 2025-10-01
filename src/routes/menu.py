from flask import Blueprint

menu_blueprint = Blueprint("menu", __name__)

@menu_blueprint.route("/", methods=["GET"])
def render_menu():
    return "render menu"

@menu_blueprint.route("/create_new_game", methods=["GET"])
def create_new_game():
    return "create new game"

@menu_blueprint.route("/load_existing_game", methods=["GET"])
def load_existing_game():
    return "load existing game"
