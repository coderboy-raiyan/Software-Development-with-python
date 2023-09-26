t = int(input())

for i in range(0, t):
    nums = input()
    sep = ''
    for n in range(0, len(nums)):
        if (n == len(nums)-1):
            sep += nums[n]
        else:
            sep += nums[n] + ' '
    print(sep[::-1])
