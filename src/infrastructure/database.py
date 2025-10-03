import sqlite3
from entities.dog import Dog

DATABASE_PATH = "./database.db"

def initialize_database():
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS games(
                uuid VARCHAR(36) PRIMARY KEY,
                dog_name VARCHAR(255) NOT NULL DEFAULT '',
                dog_bread VARCHAR(255) NOT NULL DEFAULT '',
                dog_hunger INTEGER NOT NULL DEFAULT 0,
                dog_fatigue INTEGER NOT NULL DEFAULT 0,
                dog_is_sleeping BOOLEAN NOT NULL DEFAULT TRUE,
                dog_is_dead BOOLEAN NOT NULL DEFAULT FALSE)""")
        connection.commit()

def create_game(game_uuid: str) -> None:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO games(uuid) VALUES(?)", (game_uuid,))
        connection.commit()

def update_dog_attributes(game_uuid: str, dog: Dog):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE games SET 
                dog_name = ?,
                dog_bread = ?,
                dog_hunger = ?,
                dog_fatigue = ?,
                dog_is_sleeping = ?,
                dog_is_dead = ?
            WHERE uuid = ?""", (*dog.get_status(), game_uuid))
        connection.commit()

def find_game_by_uuid(game_uuid: str):
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        game = cursor.execute("SELECT * FROM games WHERE uuid = ?", (game_uuid,)).fetchone()
    
    return game

def is_game_exist(game_uuid: str) -> bool:
    with sqlite3.connect(DATABASE_PATH) as connection:
        cursor = connection.cursor()
        game = cursor.execute("SELECT * FROM games WHERE uuid = ?", (game_uuid,)).fetchone()
    
    return game is not None