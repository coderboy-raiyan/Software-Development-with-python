def test(func):
    def inner():
        func()
        print("Inside of inner")
    return inner


@test
def getInside():
    print("Getting Inside")


getInside()
# test(getInside)()
