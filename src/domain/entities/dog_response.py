from typing import TypedDict

class DogResponse(TypedDict):
    dog_name: str
    dog_breed: str
    dog_hunger: int
    dog_fatigue: int
    dog_is_sleeping: bool
    dog_is_dead: bool
    dog_warning: str
    dog_message: str
