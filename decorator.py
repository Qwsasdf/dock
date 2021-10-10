def decor(func):
    def wrapper():
        print("before func")
        func()
        print("after func")
    return wrapper

# @decor

def f():
    print("petya")

f=decor(f)
print("dsf")
f()
