from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 6, 7, 7, 7]
sentence = "I own Vues Technologies"

# print(Counter(li))
# print(Counter(sentence))

dictionary = defaultdict(lambda: "It does not match", {'a': 1, 'b': 2})
print(dictionary['c'])

d1 = OrderedDict()
d1['a'] = 1
d1['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d1 == d2)
