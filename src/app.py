from flask import Flask
from limiter_config import limiter
from infrastructure.database import initialize_database
from routes.error_handlers import ratelimit_handler, notfound_handler
from routes.dog_api import dog_api_blueprint
from routes.menu import menu_blueprint
from routes.game import game_blueprint

app = Flask(__name__, template_folder="views/templates", static_folder="views/static")

limiter.init_app(app)

app.register_error_handler(429, ratelimit_handler)
app.register_error_handler(404, notfound_handler)

app.register_blueprint(dog_api_blueprint, url_prefix="/api/dog")
app.register_blueprint(menu_blueprint, url_prefix="/menu")
app.register_blueprint(game_blueprint, url_prefix="/game")

initialize_database()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
