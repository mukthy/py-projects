class Person:
    description = "Generic person"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("My name is {} and I'm {}".format(self.name, self.age))

    def eat(self, food):
        print("{} is eating {}".format(self.name, food))

    def action(self):
        print("{} jumps".format(self.name))


class Baby(Person):  # inherit from Person
    description = "Baby"

    def speak(self):
        print("ba ba ba")

    def nap(self):
        print("{} is napping".format(self.name))


person = Person("John", 30)
person.speak()
person.eat("pizza")
person.action()

# baby will have the same attributes as person and nap function from its own class

baby = Baby("Mary", 1)
baby.speak()
baby.eat("baby food")
baby.action()

print(person.description)
print(baby.description)
