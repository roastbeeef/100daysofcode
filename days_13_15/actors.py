# lowest level creation. stores pieces of data
from random import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level

# inheritance!
class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        # this is inheriting the attributes (meta) from the creature class
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    # this is defined here instead of inherited because we're fundamentally changing the way that a dragon defends its rolls
    def defensive_roll(self):
        # inheriting the defensive_roll method from the Create class
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breathes_fire:
            # if the dragon can breathe fire, it get a double roll
            value = value * 2

        return value

class Wizard(Creature):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return my_roll >= their_roll