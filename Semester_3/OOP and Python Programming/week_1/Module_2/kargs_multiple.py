def double_it(num1, num2, **args):
    sum = num1 + num2
    return num1, num2, args


double_it(100, 200, also=700)
