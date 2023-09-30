def powerTheNumber(number, * args):
    for i in args:
        print(number ** i)


def userInfo(userName, **kwargs):
    print(f"User : {userName}", end="\n")
    for i, v in kwargs.items():
        print(f"{i} : {v}", end="\n")


userInfo("Raiyan", age=20, passion='coding')
