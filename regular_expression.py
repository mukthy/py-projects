import re

pattern = re.compile('search this inside of this text please!')
string = 'search this inside of this text please! mukthy'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # it tries to get the exact match
d = pattern.match(string)  # it tries to find the match

# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

# print(a.group())
print(d)
