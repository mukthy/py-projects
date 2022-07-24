class Dog:  # class name is dog
    # class attributes
    species = 'mammal'  # every species object in the dog class will be created with the species mammal

    def __init__(self, name, age):
        self.name = name  # instance attributes
        self.age = age  # instance attributes
        # self is used to refer the current object being created during instantiation
