from infrastructure.database import update_dog_attributes, find_game_by_uuid
from domain.entities.dog_response import DogResponse
from domain.entities.dog import Dog

def show_dog_status_service(game) -> DogResponse:
    response = __serialize_response_from_db(game)
    return response

def wake_up_dog_service(game):
    dog = __serialize_dog_from_db(game)
    dog.wake_up()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return dog.message

def feed_dog_service(game) -> str:
    dog = __serialize_dog_from_db(game)
    dog.feed()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return dog.message

def play_with_dog_service(game) -> str:
    dog = __serialize_dog_from_db(game)
    dog.play()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return dog.message

def sleep_dog_service(game) -> str:
    dog = __serialize_dog_from_db(game)
    dog.sleep()
    update_dog_attributes(game_uuid=game[0], dog=dog)
    return dog.message

def __serialize_response_from_db(database_game_data: tuple[str, str, str, int, int, bool, bool, str]) -> DogResponse:
    response: DogResponse = {
        "dog_name": database_game_data[1],
        "dog_breed": database_game_data[2],
        "dog_hunger": database_game_data[3],
        "dog_fatigue": database_game_data[4],
        "dog_is_sleeping": database_game_data[5],
        "dog_is_dead": database_game_data[6],
        "dog_warning": database_game_data[7],
        "dog_message": database_game_data[8],
    }
    return response

def __serialize_dog_from_db(database_game_data: tuple[str, str, str, int, int, bool, bool, str]) -> Dog:
    dog = Dog(
        name=database_game_data[1], 
        breed=database_game_data[2], 
        hunger=database_game_data[3], 
        fatigue=database_game_data[4], 
        is_sleeping=database_game_data[5], 
        is_dead=database_game_data[6])
    return dog