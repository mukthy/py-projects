class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

    # instance method
    def birthday(self):
        self.age += 1


mikey = Dog("Mikey", 6)  # create a new object, instantiating the Dog class
print(mikey.description())  # call the instance method
print(mikey.speak("Woof"))  # call the instance method

mikey.birthday()

print(mikey.description())
