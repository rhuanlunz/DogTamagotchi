from flask import Flask
from infrastructure.database import initialize_database
from routes.dog_api import dog_api_blueprint
from routes.menu import menu_blueprint
from routes.game import game_blueprint

app = Flask(__name__)

app.register_blueprint(dog_api_blueprint, url_prefix="/api/dog")
app.register_blueprint(menu_blueprint, url_prefix="/menu")
app.register_blueprint(game_blueprint, url_prefix="/game")

initialize_database()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
