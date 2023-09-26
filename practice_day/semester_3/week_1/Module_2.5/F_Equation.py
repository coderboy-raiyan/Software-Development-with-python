x, n = input().split()

x = int(x)
n = int(n)

s = 0


def sumOfNums(n, x):
    global s
    s = 0
    if (n == 0 or x == 0):
        print(s)
        return
    for i in range(1, n+1):
        if (i % 2 == 0):
            pow = x ** i
            s += pow
    print(s)


sumOfNums(n, x)
