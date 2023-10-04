class Person:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, weight, team) -> None:
        self.team = team
        super().__init__(name, age, weight)

    def __add__(self, other):
        return self.age + other.age


shanto = Cricketer("Shanto", 28, 65, "BD")
mehedi = Cricketer("Mehedi Miraz", 28, 68, "BD")

print(shanto + mehedi)
