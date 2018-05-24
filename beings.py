from string import capwords

class Being():
    'Abstract base class for all living characters in the game'

    _being_count = 0

    # Private attributes:
    # _name 
    # _home
    # _vitality
    # _dexterity
    # _agility 
    # _experience

    def __init__(self, name, home):
        Being._being_count += 1
        self._name = capwords(name)
        self._home = capwords(home)
        self._vitality = 0
        self._dexterity = 0
        self._agility = 0
        self._experience = 1
    
    def get_full_name(self):
        return self._name + " of " + self._home

    def get_vitality(self):
        return self._vitality

    def set_vitality(self, vitality):
        self._vitality = vitality

    def get_dexterity(self):
        return self._dexterity

    def set_dexterity(self, dexterity):
        self._dexterity = dexterity

    def get_agility(self):
        return self._agility

    def set_agility(self, agility):
        self._agility = agility

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience


class Human(Being):

    _human_count = 0

    def __init__(self, name, home):
        super().__init__(name, home)
        Human._human_count += 1
        self._vitality = 5
        self._dexterity = 5
        self._agility = 5


class Gnome(Being):

    _gnome_count = 0

    def __init__(self, name, home):
        super().__init__(name, home)
        Gnome._gnome_count += 1
        self._vitality = 4
        self._dexterity = 5
        self._agility = 6


class Cyclops(Being):

    _cyclops_count = 0

    def __init__(self, name, home):
        super().__init__(name, home)
        Cyclops._cyclops_count += 1   
        self._vitality = 6
        self._dexterity = 4
        self._agility = 5


class Elf(Being):

    _elf_count = 0

    def __init__(self, name, home):
        super().__init__(name, home)
        Elf._elf_count += 1   
        self._vitality = 5
        self._dexterity = 6
        self._agility = 4


myBeing = Human("crAig", "Aberdeen")
print(myBeing.get_full_name())
