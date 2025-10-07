from flask import Blueprint, jsonify, redirect, url_for
from werkzeug.exceptions import NotFound, TooManyRequests

error_handler_blueprint = Blueprint("error_handler", __name__)

@error_handler_blueprint.errorhandler(TooManyRequests)
def ratelimit_handler(e):
    return jsonify({"error": "Calma aí, chefe. É muita request... Dá uma segurada."}), TooManyRequests

@error_handler_blueprint.errorhandler(NotFound)
def notfound_handler(e):
    return redirect(url_for("menu.render_menu"))
