# (0,1,1,2,3,5,8,13)
# using Generators
def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a

        #print(f'this is a {a}')
        a = b
        #print(f'this is b {b}')
        b = temp + b


for x in fib(21):
    print(x)

# using List


def fib_list(number):
    first = 0
    second = 1
    result = []
    for i in range(number):
        result.append(first)
        temp = first
        first = second
        second = temp + second
    return result


print(fib_list(21))
