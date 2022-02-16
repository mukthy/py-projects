
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cat_details(self):
        self.name = input("Enter Cats Name")
        self.age = int(input("Enter Age"))

# 1 Instantiate the Cat object with 3 cats


# cat1 = 10
# cat2 = 20
# cat3 = 5

cat1 = Cat('first', 6)
cat2 = Cat('second', 7)
cat3 = Cat('third', 5)


def oldest(*args):
    return max(args)


print(f"The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old")
