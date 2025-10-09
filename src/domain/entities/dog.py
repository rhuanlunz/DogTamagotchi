from domain.exceptions.is_dead_exception import IsDeadException
from domain.exceptions.is_sleeping_exception import IsSleepingException
from domain.exceptions.not_hungry_exception import NotHungryException
from domain.exceptions.not_tired_exception import NotTiredException
from domain.exceptions.already_awake_exception import AlreadyAwakeException

class Dog:
    def __init__(self, name: str, breed: str, hunger: int = 0, fatigue: int = 0, is_sleeping: bool = True, is_dead: bool = False) -> None:
        self.name = name.strip().capitalize()
        self.breed = breed.strip().capitalize()
        self.hunger = hunger
        self.fatigue = fatigue
        self.is_sleeping = is_sleeping
        self.is_dead = is_dead
        self.warning = ""
        self.message = ""
        self.MAX_HUNGER = 6
        self.MAX_FATIGUE = 5

    def get_status(self):
        return (self.name, 
                self.breed, 
                self.hunger, 
                self.fatigue,
                self.is_sleeping, 
                self.is_dead, 
                self.warning,
                self.message)

    def wake_up(self) -> None:
        if self.is_dead:
            raise IsDeadException(f"{self.name} tá morto...")
        
        if not self.is_sleeping:
            raise AlreadyAwakeException(f"{self.name} já tá acordado.")
        
        self.is_sleeping = False
        self.message = f"{self.name} acordou!"

    def feed(self) -> None:
        if self.is_dead:
            raise IsDeadException(f"{self.name} tá morto...")
        
        if self.is_sleeping:
            raise IsSleepingException(f"Como que come dormindo?")
        
        if self.hunger == 0:
            raise NotHungryException(f"Quer deixar o {self.name} gordo, é?")
        
        self.hunger = 0
        self.message = f"{self.name} foi alimentado!"

    def play(self) -> None:
        if self.is_dead:
            raise IsDeadException(f"{self.name} tá morto...")
        
        if self.is_sleeping:
            raise IsSleepingException(f"Como que brinca dormindo?")
        
        self.hunger += 1
        if self.hunger == self.MAX_HUNGER:
            self.__die()
            return
        elif self.hunger == self.MAX_HUNGER - 1:
            self.warning = f"{self.name} pode morrer em breve..."
        
        self.fatigue += 1
        if self.fatigue == self.MAX_FATIGUE:
            self.sleep()
            return

        self.message = f"{self.name} jogou GTA 6!"
 
    def sleep(self) -> None:
        if self.is_dead:
            raise IsDeadException(f"{self.name} está dormindo, para sempre...")

        if self.is_sleeping:
            raise IsSleepingException(f"{self.name} já tá cortando no sono.")
        
        if self.fatigue == 0:
            raise NotTiredException(f"{self.name} não está cansado.")

        self.is_sleeping = True
        self.fatigue = 0
        self.message = f"{self.name} cortou no sono..."

    def __die(self) -> None:
        self.is_dead = True
        self.warning = ""
        self.message = f"{self.name} morreu KKKKKKKKK"
