class Being():
    'Base class for all living characters in the game'

    name = ""
    home = ""
    vitality = 0
    dexterity = 0
    agility = 0
    experience = 0
    # INIT AND GET/SET/CHANGE FOR EXPERIENCE

    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.experience = 1
    
    def get_full_name(self):
        return self.name + " of " + self.home

    def get_vitality(self):
        return self.vitality

    def set_vitality(self, vitality):
        self.vitality = vitality

    def get_dexterity(self):
        return self.dexterity

    def set_dexterity(self, dexterity):
        self.dexterity = dexterity

    def get_agility(self):
        return self.agility

    def set_agility(self, agility):
        self.agility = agility


class Human(Being):

    def __init__(self, name, home, vitality, dexterity, agility):
        super().__init__(name, home)
        self.vitality = 5
        self.dexterity = 5
        self.agility = 5


myBeing = Human("Craig", "Aberdeen")
print(myBeing.get_full_name())
