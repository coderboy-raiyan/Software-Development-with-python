def double_it(*args):
    res = 0
    for num in args:
        res += num
    return res


print(double_it(10, 20, 30, 800))
