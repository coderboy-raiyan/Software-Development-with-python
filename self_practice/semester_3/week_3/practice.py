import re
from collections import Counter


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
