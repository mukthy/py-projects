# Generator: It allows us to generate a sequence of values over time.

range(100)  # Generator

# Generators allows us to use a keyword in python called yield.

# yield pauses the function and comes back to it when we do something to it which is next().
# all generators are iterables but not every iterable is a generator.
# range(100) is a generator which is iterable but list() is a iterable but not a generator.
# So, generator is a subset of iterable.


def generator_function(num):
    for i in range(num):
        yield i*2


for item in generator_function(10):
    print(item)


def generator_function(num):
    for i in range(num):
        yield i*2


g = generator_function(10)
next(g)
next(g)
# next(g) actually remembers the last iterated value in the memory in this case it is 2.
print(next(g))


def special_for(iterable):
    # this is an iter function which allows us to use the next() function
    iterator = iter(iterable)
    while True:
        try:
            # print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break


special_for([1, 2, 3])

# create a class MyGen()


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num*2

        raise StopIteration


gen = MyGen(0, 8)
for i in gen:
    print(i)
