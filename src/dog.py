class Dog:
    def __init__(self, name: str, breed: str) -> None:        
        self.name = name.strip().capitalize()
        self.breed = breed.strip().lower()
        self.hunger = 0
        self.fatigue = 0
        self.MAX_HUNGER = 6
        self.MAX_FATIGUE = 5
        self.sleeping = True
        self.dead = False

    def wake_up(self) -> None:
        if not self.__is_sleeping():
            raise Exception(f"{self.name} is already awake.")
        
        if not self.__is_alive():
            raise Exception(f"{self.name} cannot wake up, he died...")
        
        self.sleeping = False
        print(f"{self.name} wake up!")

    def feed(self) -> None:
        if self.hunger < self.MAX_HUNGER - 4:
            raise Exception(f"{self.name} doesn't need to eat.")

        if self.__is_sleeping():
            raise Exception(f"{self.name} cannot eat, he's sleeping.")
        
        if not self.__is_alive():
            raise Exception(f"{self.name} cannot eat, he died...")
        
        self.hunger = 0
        print(f"{self.name} received food!")

    def play(self) -> None:
        if self.__is_sleeping():
            raise Exception(f"{self.name} cannot play, he's sleeping.")
        
        if not self.__is_alive():
            raise Exception(f"{self.name} cannot play, he died...")
        
        self.hunger += 1
        if self.hunger == self.MAX_HUNGER:
            self.__die()
            return
        elif self.hunger == self.MAX_HUNGER - 1:
            print(f"{self.name} may die soon...")
        
        self.fatigue += 1
        if self.fatigue == self.MAX_FATIGUE:
            self.sleep()
            return
        
        print(f"{self.name} played!")

    def show_status(self) -> tuple[str, str, int, int, bool, bool]:
        return (self.name, self.breed, self.hunger, self.fatigue, self.sleeping, self.dead)
    
    def sleep(self) -> None:
        if self.fatigue < self.MAX_FATIGUE - 3:
            raise Exception(f"{self.name} doesn't need to sleep.")

        if self.__is_sleeping():
            raise Exception(f"{self.name} is already sleeping.")
        
        if not self.__is_alive():
            raise Exception(f"{self.name} is already sleeping. For ever...")

        self.sleeping = True
        self.fatigue = 0
        print(f"{self.name} is sleeping...")

    def __is_sleeping(self) -> bool:
        return self.sleeping
    
    def __is_alive(self) -> bool:
        return not self.dead

    def __die(self) -> None:
        self.dead = True
        print(f"{self.name} died...")
