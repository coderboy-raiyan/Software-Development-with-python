from collections import *

n = input()

nums = list(map(int, input().split()))
cntList = Counter(nums)

cnt = 0

for i, k in cntList.items():
    if (i > k):
        cnt += k
    else:
        cnt += abs(k-i)

print(cnt)
