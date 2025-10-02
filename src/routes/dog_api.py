from flask import Blueprint, request, jsonify
from infrastructure.database import find_game_by_uuid

dog_api_blueprint = Blueprint('dog_api', __name__)

@dog_api_blueprint.route("/status", methods=["GET"])
def show_dog_status():
    game_save = request.args.get("save")
    if game_save is None:
        return "Save parameter is none", 400

    game = find_game_by_uuid(game_save)
    if game is None:
        return "Inexistent game", 404
    
    response = {
        "dog_name": game[1],
        "dog_bread": game[2],
        "dog_hunger": game[3],
        "dog_fatigue": game[4],
        "dog_is_sleeping": game[5],
        "dog_is_dead": game[6]
    }

    return jsonify(response), 200

@dog_api_blueprint.route("/wake_up", methods=["GET"])
def wake_up_dog():
    return "wake up"

@dog_api_blueprint.route("/feed", methods=["GET"])
def feed_dog():
    return "feed"

@dog_api_blueprint.route("/play", methods=["GET"])
def play_with_dog():
    return "play"

@dog_api_blueprint.route("/sleep", methods=["GET"])
def sleep_dog():
    return "sleep"
