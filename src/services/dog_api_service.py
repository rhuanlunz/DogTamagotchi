from infrastructure.database import update_dog_attributes, find_game_by_uuid
from entities.dog_response import DogResponse
from entities.dog import Dog

def show_dog_status_service(game_uuid: str | None) -> DogResponse:
    game = find_game_by_uuid(game_uuid)
    response = __serialize_response_from_db(game)
    return response

def wake_up_dog_service(game_uuid: str | None) -> str:
    game = find_game_by_uuid(game_uuid)
    dog = __serialize_dog_from_db(game)
    dog.wake_up()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return f"{dog.name} waked up!"

def feed_dog_service(game_uuid: str | None) -> str:
    game = find_game_by_uuid(game_uuid)
    dog = __serialize_dog_from_db(game)
    dog.feed()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return f"{dog.name} received food!"

def play_with_dog_service(game_uuid: str | None) -> str:
    game = find_game_by_uuid(game_uuid)
    dog = __serialize_dog_from_db(game)
    dog.play()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return f"{dog.name} played!"

def sleep_dog_service(game_uuid: str | None) -> str:
    game = find_game_by_uuid(game_uuid)
    dog = __serialize_dog_from_db(game)
    dog.sleep()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return f"{dog.name} is sleeping..."

def __serialize_response_from_db(database_game_data: tuple[str, str, str, int, int, bool, bool]) -> DogResponse:
    response: DogResponse = {
        "dog_name": database_game_data[1],
        "dog_bread": database_game_data[2],
        "dog_hunger": database_game_data[3],
        "dog_fatigue": database_game_data[4],
        "dog_is_sleeping": database_game_data[5],
        "dog_is_dead": database_game_data[6]
    }
    return response

def __serialize_dog_from_db(database_game_data: tuple[str, str, str, int, int, bool, bool]) -> Dog:
    dog = Dog(
        name=database_game_data[1], 
        breed=database_game_data[2], 
        hunger=database_game_data[3], 
        fatigue=database_game_data[4], 
        sleeping=database_game_data[5], 
        dead=database_game_data[6])
    return dog