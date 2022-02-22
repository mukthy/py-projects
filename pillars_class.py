# Pillars of Class
# Encapsulation: It is the binding of data and functions that modifies that data.
# we encapsulate it into on big object, so that we can put them into a single box.

# Abstraction: Hiding of information or abstracting away information and giving access to information what is necessary.

import email


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f"My name is {self.name} and my age is {self.age}")


player1 = PlayerCharacter('Mukthy', 100)
# In abstraction, when I call speak I do not really care how speak is implemented.
player1.speak()
# same happens with tuple:

print((1, 2, 3, 1).count(1))

# private variables: There is no privacy in Python. To overcome this we need to give _ 'Underscore' infront of the variable. ex: self._name or self._age.


class PlayerCharacters:
    def __init__(self, name1, age1):
        # private variable since it has _ 'underscore' it just a naming convention and it does not have any special powers.
        self._name1 = name1
        self._age1 = age1

    def run(self):
        print('run')

    def speak(self):
        print(f"My name is {self._name1} and my age is {self._age1}")


player2 = PlayerCharacters('Mukthy', 100)
# In abstraction, when I call speak I do not really care how speak is implemented.
player2.speak()
# same happens with tuple:


# Inheritence: It allows new objects to take on the properties of existing objects, So we can inherit classes.

class User():

    # if there are no attributes or variable the we do not need __init__ method.
    def sign_in(self):
        return 'logged in'

# in-order to inherit the User class we just need to pass the the class name "User" in the brackets ex: class Archer(User):.


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


# inherting the class user.


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
# wizard1.attack()
print(archer1.sign_in())

# sometimes the Wizard and Archer classes are called subclasses or child classes or derived classes.

# to check instanse is part of the class.

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, Archer))

# python comes with an object base class, where every created class is a subclass of class object.

print(isinstance(wizard1, object))

# Polymorphism: It means many forms. In polymorphism we can share same method names, because of the object that they are calling the output will be different.
# Polymorphism allows us to have many forms it is the ability to redefine method for these derived classes that is Wizard and Archer, An object which gets instanciated can behave in different form.


class User():

    # if there are no attributes or variable the we do not need __init__ method.
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        return 'logged in'

    def attack(self):
        print('Do nothing')


class Wizard(User):
    def __init__(self, name, power, email):
        # this is mentioned if we want to get the attributes of USer class.
        # super refers to the parent class which above the wizard for now.
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):  # same method name as of class Archer
        # if we also want to use the attack method from the User class then we can mention like this after inheriting User class.
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):  # same method name as of class Wizard
        print(f'attacking with arrows: arrows left {self.num_arrows}')


class Emails(User):
    def emails(self, email):
        print(email)


wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100)
emails = Emails('This is from Email Class: merlin@gmail.com')
wizard1.attack()  # same method name but used with different objects
archer1.attack()  # same method name but used with different objects
print(emails.email)


# def player_attack(char):
#    char.attack()


# print(wizard1)
# player_attack(wizard1)
# player_attack(archer1)

# for character in [wizard1, archer1]:
#    print(character)
#    character.attack()
