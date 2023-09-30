from collections import Counter
import re
nums = [10, 100, 200]
mx = nums[0]
for i in nums:
    if i > mx:
        mx = i
print(mx)

for i in range(0, 20):
    if i % 2 != 0:
        print(i)


txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")
strList = list(x)

strTuple = "Raiyan", "Turno", False
strList = list(strTuple)


email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'


def is_valid_email(email):
    if (re.match(email_pattern, email)):
        return "Yaay!! it's a valid mail"
    else:
        return "Oops!! Bad email 🤧😭"


email = input("Give me your email ")
print(is_valid_email(email))
