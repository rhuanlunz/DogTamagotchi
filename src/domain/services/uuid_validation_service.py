from infrastructure.database import is_game_exist
from uuid import UUID

def validate_game_uuid_service(game_uuid: str | None) -> None:
    if not game_uuid:
        raise Exception("Invalid game UUID or game does not exist.")

    try:
        UUID(game_uuid)
    except ValueError:
        raise Exception("Invalid game UUID or game does not exist.")

    if not is_game_exist(game_uuid):
        raise Exception("Invalid game UUID or game does not exist.")
    