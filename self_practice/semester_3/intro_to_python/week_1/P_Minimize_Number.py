n = int(input())

nums = list(map(int, input().split()))


cnt = 0
while True:
    all_even = True
    for num in nums:
        if (num % 2 != 0):
            all_even = False

    if (all_even):
        cnt += 1
        for i in range(n):
            if (nums[i] % 2 == 0):
                nums[i] = nums[i] // 2
    else:
        break

print(cnt)
