from flask import Blueprint

dog_api_blueprint = Blueprint('dog_api', __name__)

@dog_api_blueprint.route("/status", methods=["GET"])
def show_dog_status():
    return "show status"

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
