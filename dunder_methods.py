#Dunder Methods:

# it is a special method. They allow us to use python specific functions on objects created through our class.

#For ex: len([1,2,3])

class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {
            'name': 'sarah',
            'have_pet': False
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5

    def __call__(self):
        return('yesss??')

    def __getitem__(self, i):
        return self.dict[i]

action_figure = Toy('red', 29)
#print(action_figure.__call__)
print(action_figure())
print(len(action_figure))
print(action_figure.__len__)
print(str(action_figure))
print(action_figure.__str__)
print(action_figure.dict['name'])
    