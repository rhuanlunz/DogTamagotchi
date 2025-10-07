from flask import Blueprint, request, jsonify, abort, g
from limiter_config import limiter
from domain.services.uuid_validation_service import *
from domain.services.dog_api_service import *

dog_api_blueprint = Blueprint('dog_api', __name__)

@dog_api_blueprint.before_request
def validate_game_uuid_middleware():
    game_save = request.args.get("save")
    try:
        validate_game_uuid_service(game_save)
        g.game_save = game_save
    except Exception as e:
        abort(400, description=str(e))

@dog_api_blueprint.route("/status", methods=["GET"])
@limiter.limit("5/second")
def show_dog_status():
    try:
        response = show_dog_status_service(g.game_save)
    except Exception as e:
        return jsonify(str(e)), 400
    
    return jsonify(response), 200

@dog_api_blueprint.route("/wake_up", methods=["GET"])
@limiter.limit("5/second")
def wake_up_dog():
    try:
        message = wake_up_dog_service(g.game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/feed", methods=["GET"])
@limiter.limit("5/second")
def feed_dog():
    try:
        message = feed_dog_service(g.game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/play", methods=["GET"])
@limiter.limit("5/second")
def play_with_dog():
    try:
        message = play_with_dog_service(g.game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200

@dog_api_blueprint.route("/sleep", methods=["GET"])
@limiter.limit("5/second")
def sleep_dog():
    try:
        message = sleep_dog_service(g.game_save)
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": message}), 200
