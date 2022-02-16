# CLASS
# Objects

# Class is a paradigm.

# instanciate a class meaning, calling the class to create an object.

class BigObject:  # class
    pass


obj1 = BigObject()  # instanciate
print(obj1)

# Self keyword is a way for us to define the self. Self refers to the class name (ie, PlayerCharacter)
# Self refers to the PlayerCharacter that we are going to create a player1 object


class PlayerCharacter:
    # Class Object Attribute which is not dynamic (i.e, static) All the objects player1 and player2 will have the same value.
    # It is used when we do not want to change the value and keep the same value for all the objects.
    membership = True

    # __init__ is a constructor function. It runs on every class instaciation so that we can customize our objects.
    def __init__(self, name, age):
        if (self.membership):
            # atributes these are also the properties of the class. Name and Age is the properties / attributes of the class.
            # These attributes are dynamic, meaning we can pass the value as argument and it can be different for different objects.
            self.name = name
            self.age = age

    def run(self):
        # here we cannot use the PlayerCharacter.name/age because the name and age is not a Class Object Attribute.
        print(f"My Name is {self.name}, my age is {self.age}")
        # here membership is part of the Class Object Attribute, even using self.membership will also work becuase self refers to the class PlayerCharacter.
        print(f"My Membership is {PlayerCharacter.membership}")
        print(f"My Membership is {self.membership}")
        return 'done'


player1 = PlayerCharacter('Cindy', 55)  # instanciate the class.
player2 = PlayerCharacter('Mukthy', 30)
player2.attack = 500

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player2.attack)
print(player1.run())
print(player2.run())

# we can create multiple objects for the same class.

# Syntax


class NameOfClass():
    class_attribute = 'value'

    def _init_(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        # code
        pass

    @classmethod
    def cls_method(cls, param1, param2):
        # code
        pass

    @staticmethod
    def stc_method(param1, param2):
        # code
        pass
