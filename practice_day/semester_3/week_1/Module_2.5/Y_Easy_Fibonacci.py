n = int(input())


dp = [-1]*100

arr = [0, 1, 1]


def fib(n):
    if (n <= 1):
        return 1
    if (dp[n] != -1):
        return dp[n]
    ans1 = fib(n-1)
    ans2 = fib(n-2)
    dp[n] = ans1 + ans2
    arr.append(dp[n])
    return dp[n]


fib(n)

for i in range(0, n):
    print(arr[i], end=' ')
