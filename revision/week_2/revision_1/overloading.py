class Person():
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        super().__init__(name, age, height, weight)
        self.team = team

    def __add__(self, other):
        return self.age + other.age

    def __mul__(self, other):
        return self.height * other.weight


shakib = Cricketer("Shakib", 36, 120, 76, "BD")
shanto = Cricketer("Shanto", 32, 124, 55, "BD")

print(shakib * shanto)
