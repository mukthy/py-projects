class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if (self.membership):
            self.name = name
            self.age = age

    def run(self):
        print(f"My Name is {self.name}, my age is {self.age}")
        print(f"My Membership is {PlayerCharacter.membership}")
        print(f"My Membership is {self.membership}")
        return 'done'

    # classmethod is actually a method for class where we do not need to create an object to use it.
    @classmethod
    # cls here is refering to the class name just like a self would do.
    def add_func(cls, num1, num2):
        return num1 + num2

# we can use cls to instanciate the class like below:
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1 + num2)

    # static method does not have cls and will not have access to class.
    @staticmethod
    # it is used when we do not care about the class state, for ex: age and name.
    def adding_things2(num1, num2):
        return num1 + num2

# classmethod is used when we want to access the class and probably want to modify the state or values. Static Method is used when we do not care about the class state.


# if classmethod is used then we can simply use the classname with the function.
print(PlayerCharacter.add_func(3, 5))

# this is the cls instanciate object where we are passing 5,6 which will be added and accessing the class state.
player3 = PlayerCharacter.adding_things(5, 6)
print(player3.name, player3.age)

# player1 = PlayerCharacter('Cindy', 55)  # instanciate the class.
#player2 = PlayerCharacter('Mukthy', 30)
#player2.attack = 500

#print(player1.name, player1.age)
#print(player2.name, player2.age)
# print(player2.attack)
# print(player1.run())
# print(player2.run())

# we can create multiple objects for the same class.
