# nonlocal Keyword

def outer():
    x = "local"

    def inner():
        # when we use non-local it will use the parent scope and also modify the value of x to "non-local" which is in the parent.
        nonlocal x
        x = "non-local"
        print("inner:", x)
    inner()
    print("outer:", x)


outer()

# excercise
x = 'hello'[0]
print(x)

x = x.replace()
