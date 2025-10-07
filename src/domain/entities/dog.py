class Dog:
    def __init__(self, name: str, breed: str, hunger: int = 0, fatigue: int = 0, sleeping: bool = True, dead: bool = False) -> None:
        self.name = name.strip().capitalize()
        self.breed = breed.strip().capitalize()
        self.hunger = hunger
        self.fatigue = fatigue
        self.sleeping = sleeping
        self.dead = dead
        self.warning_message = ""
        self.MAX_HUNGER = 6
        self.MAX_FATIGUE = 5

    def get_status(self):
        if self.hunger == self.MAX_HUNGER - 1:
            self.warning_message = f"{self.name} pode morrer em breve..."

        return (self.name, 
                self.breed, 
                self.hunger, 
                self.fatigue,
                self.sleeping, 
                self.dead, 
                self.warning_message)

    def wake_up(self) -> None:
        if not self.__is_alive():
            raise Exception(f"{self.name} tá morto...")
        
        if not self.__is_sleeping():
            raise Exception(f"{self.name} já tá acordado.")
        
        self.sleeping = False

    def feed(self) -> None:
        if not self.__is_alive():
            raise Exception(f"{self.name} tá morto...")
        
        if self.__is_sleeping():
            raise Exception(f"Como que come dormindo?")
        
        if self.hunger == 0:
            raise Exception(f"Quer deixar o {self.name} gordo, é?")
                
        self.hunger = 0

    def play(self) -> None:
        if not self.__is_alive():
            raise Exception(f"{self.name} tá morto...")
        
        if self.__is_sleeping():
            raise Exception(f"Como que brinca dormindo?")
        
        self.hunger += 1
        if self.hunger == self.MAX_HUNGER:
            self.__die()
            return
        
        self.fatigue += 1
        if self.fatigue == self.MAX_FATIGUE:
            self.sleep()
 
    def sleep(self) -> None:
        if not self.__is_alive():
            raise Exception(f"{self.name} está dormindo, para sempre...")

        if self.__is_sleeping():
            raise Exception(f"{self.name} já tá cortando no sono.")
        
        if self.fatigue == 0:
            raise Exception(f"{self.name} não está cansado.")

        self.sleeping = True
        self.fatigue = 0

    def __is_sleeping(self) -> bool:
        return self.sleeping
    
    def __is_alive(self) -> bool:
        return not self.dead

    def __die(self) -> None:
        self.warning_message = f"{self.name} morreu KKKKKKKKK"
        self.dead = True
        
