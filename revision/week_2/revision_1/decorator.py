import math


def timer(func):
    def inner(*args):
        print("timer started")
        func(*args)
        print("timer end")
    return inner


@timer
def get_factorial(i):
    fact = math.factorial(i)
    print(fact)


get_factorial(3)
