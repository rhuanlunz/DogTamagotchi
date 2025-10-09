from domain.exceptions.invalid_uuid_format_exception import InvalidUUIDFormatException
from domain.exceptions.game_not_exists_exception import GameNotExistsException
from infrastructure.database import is_game_exist
from uuid import UUID

def validate_game_uuid_service(game_uuid: str | None) -> None:
    if not game_uuid:
        raise Exception("Game UUID parameter cannot be null.")

    try:
        UUID(game_uuid)
    except ValueError:
        raise InvalidUUIDFormatException("O Formato do UUID é inválido.")

    if not is_game_exist(game_uuid):
        raise GameNotExistsException("Este jogo não existe.")
    