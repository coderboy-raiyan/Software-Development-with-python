n = int(input())

nums = list(map(int, input().split()))

cnt = 0
while True:
    all_even = True
    for num in nums:
        if num % 2 != 0:
            all_even = False
            break
    if all_even:
        for i in range(n):
            nums[i] = nums[i] // 2
        cnt += 1
    else:
        break

print(cnt)
