from flask import Blueprint, request, jsonify, abort
from services.uuid_validation_service import *
from services.dog_api_service import *

dog_api_blueprint = Blueprint('dog_api', __name__)

@dog_api_blueprint.before_request
def validate_game_uuid():
    game_save = request.args.get("save")
    try:
        validate_game_uuid_service(game_save)
    except Exception as e:
        abort(400, description=str(e))

@dog_api_blueprint.route("/status", methods=["GET"])
def show_dog_status():
    game_save = request.args.get("save")
    try:
        response = show_dog_status_service(game_save)
    except Exception as e:
        return jsonify(str(e)), 400
    
    return jsonify(response), 200

@dog_api_blueprint.route("/wake_up", methods=["GET"])
def wake_up_dog():
    game_save = request.args.get("save")
    try:
        message = wake_up_dog_service(game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/feed", methods=["GET"])
def feed_dog():
    game_save = request.args.get("save")
    try:
        message = feed_dog_service(game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/play", methods=["GET"])
def play_with_dog():
    game_save = request.args.get("save")
    try:
        message = play_with_dog_service(game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/sleep", methods=["GET"])
def sleep_dog():
    game_save = request.args.get("save")
    try:
        message = sleep_dog_service(game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200
