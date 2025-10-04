from infrastructure.database import create_game
from uuid import uuid4

def create_new_game_service():
    game_uuid_str = str(uuid4())
    create_game(game_uuid_str)
    return game_uuid_str
