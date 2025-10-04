from infrastructure.database import find_game_by_uuid
from uuid import UUID

def get_validated_game(game_uuid: str | None):
    if not is_valid_uuid(game_uuid):
        raise Exception("Invalid game UUID or game does not exist.")
    
    game = find_game_by_uuid(game_uuid)
    if game is None:
        raise Exception("Invalid game UUID or game does not exist.")
    
    return game

def is_valid_uuid(uuid: str | None) -> bool:
    if not uuid:
        return False

    try:
        UUID(uuid)
    except ValueError:
        return False
    
    return True