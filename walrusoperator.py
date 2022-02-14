# walrus operator ":="
# it assigns values to variable as a part of a larger expression.
# it is motsly used in if or while loops.

a = 'hellooooooooo'
if ((n := len(a)) > 10):
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    # print(n)
    a = a[:-1]
print(a)
