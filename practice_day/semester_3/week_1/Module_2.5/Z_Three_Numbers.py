k, s = map(int, input().split())


def determine_combination(k, s):
    count = 0
    for K in range(0, k+1):
        for Y in range(0, k+1):
            Z = s - K - Y
            if (0 <= Z <= k):
                count += 1
    print(count)


determine_combination(k, s)
