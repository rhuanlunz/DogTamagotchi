from entities.dog_request import DogRequest
from infrastructure.database import create_game
from uuid import uuid4

def create_new_game_service(request_data: DogRequest) -> str:
    dog_name_raw: str | None = request_data.get("dog_name")
    dog_breed_raw: str | None = request_data.get("dog_breed")

    if not dog_name_raw:
        raise Exception("dog_name request parameter is null")
    
    if not dog_breed_raw:
        raise Exception("dog_breed request parameter is null")
  
    dog_name = dog_name_raw.strip().capitalize()
    dog_breed = dog_breed_raw.strip().capitalize()
    game_uuid_str = str(uuid4())
    create_game(game_uuid_str, dog_name, dog_breed)
    return game_uuid_str

