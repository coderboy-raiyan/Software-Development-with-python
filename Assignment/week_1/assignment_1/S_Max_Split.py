s = input()

mxL = 0
mxR = 0
cnt = 0
strings = []

for c in s:
    if c == 'L':
        mxL += 1
    else:
        mxR += 1
    if mxL == mxR:
        cnt += 1
        strings.append(s[:mxL+mxR])
        s = s[mxL+mxR:]
        mxL = 0
        mxR = 0

print(cnt)
for string in strings:
    print(string)