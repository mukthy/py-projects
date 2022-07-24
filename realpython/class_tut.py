class Dog:  # class name is dog
    # class attributes
    species = 'mammal'  # every species object in the dog class will be created with the species mammal

    def __init__(self, name, age):
        self.name = name  # instance attributes
        self.age = age  # instance attributes
        # self is used to refer the current object being created during instantiation


# create a new variable called philo and assign it to a new object, instantiating the Dog class


philo = Dog('Philo', 5)
mikey = Dog('Mikey', 6)

mikey.age = 7
philo.species = 'fish'

# access the name and age attributes of the Dog object

print("{} is {} and {} is {}".format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == 'mammal':
    print("{} is a {}".format(philo.name, philo.species))
