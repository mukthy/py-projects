# Multiple Inheritence:

from unicodedata import name
from numpy import power


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attack with the prower of {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')


# This is the part of Multple Inheritence, This makse the code more complicated.

class Mukthy(Wizard, Archer):
    def __init__(self, name, arrows, power):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


mukthy = Mukthy('nathan', 50, 100)
print(mukthy.attack())
print(mukthy.check_arrows())
print(mukthy.sign_in())
