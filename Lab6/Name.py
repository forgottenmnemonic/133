class character:
    # Variables are declared and are set to private
    # using __
    __name = ""
    __HP = 0
    __AP = 0
    __race = ""

    def __init__(self, name, HP, AP, race):
        # taking information passed via arguments
        # and putting it into our objects
        self.__name = name
        self.__HP = HP
        self.__AP = AP
        self.__race = race

    def get_name(self):
        return self.__name

    def get_HP(self):
        return self.__HP

    def get_AP(self):
        return self.__AP

    def get_race(self):
        return self.__race

    def set_name(self, name):
        self.__species = name

    def set_HP(self, HP):
        self.__HP = HP

    def set_AP(self, AP):
        self.__AP = AP

    def set_race(self, race):
        self.__race = race

    def attack(self, target):
        damage = self.__AP
        print(f"{self.__name} attacks {target.__name} for {damage} damage.")
        target.receive_damage(damage)

    def receive_damage(self, damage):
        self.__HP -= damage
        if self.__HP <= 0:
            print(f"{self.__name} has been defeated!\n")
        else:
            print(f"{self.__name} receives {damage} damage. Remaining health: {self.__HP}.\n")

    def show_stats(self):
        if character.get_HP(self) <= 0:
            print(f"{character.get_name(self)} is dead")
        else:
            print(
                f"{character.get_name(self)} is a {character.get_race(self)} with {character.get_HP(self)} and "
                f"{character.get_AP(self)} AP.\n")

    def level_up(self):
        self.__AP += 10
        print(f"{character.get_name(self)} has leveled up and has {character.get_AP(self)} attack power!\n")