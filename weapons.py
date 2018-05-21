import math

class Weapon():

    damage = 0
    durability = 0

    def __init__(self):
        pass

    def get_damage(self):
        return self.damage

    def set_damage(self, damage):
        self.damage = damage

    def change_damage(self, change):
        self.damage += change


class NaturalWeapon(Weapon):

    quantity = 0

    def __init__(self, quantity):
        super().__init__(self)
        self.durability = math.inf
        self.quantity = quantity
        

class PhysicalWeapon(Weapon):

    name = ""

    def __init__(self, name=None):
        super().__init__(self)

        if self.name == None:
            self.name = "__name__"
        else:
            self.name = name

    def get_durability(self):
        return self.durability

    def set_durability(self, durability):
        self.durability = durability

    def change_durability(self, change):
        self.durability += change


class Fist(NaturalWeapon):

    def __init__(self, quantity):
        super().__init__(self, quantity)
        self.damage = 5