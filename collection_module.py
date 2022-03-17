from collections import Counter, defaultdict, OrderedDict
import pdb

li = [1, 2, 3, 4, 5, 6, 6, 7, 7, 7]
sentence = "I own Vues Technologies"

print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: "It does not match", {'a': 1, 'b': 2})
print(dictionary['c'])
# orderedDict() actually checks if the 2 dicts are equal but it will also check if they are in correct order.
d1 = OrderedDict()
dic1 = {'c': 100, 'd': 200}
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2
dic2 = {'d': 200, 'c': 100}
print(dic2)


def add(num1, num2):
    pdb.set_trace()
    return num1 + num2


add(5, 4)
