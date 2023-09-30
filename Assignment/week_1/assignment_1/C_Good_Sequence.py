from collections import Counter

n = int(input())
lst = list(map(int, input().split()))

cntList = Counter(lst)
cnt = 0

for k, v in cntList.items():
    if k > v:
        cnt += v
    else:
        cnt += abs(v - k)

print(cnt)
