class Family:
    def __init__(self, address) -> None:
        self.address = address


class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level


class Sports:
    def __init__(self, favoriteSport) -> None:
        self.sport = favoriteSport


class Student(Family, School, Sports):
    def __init__(self, address, id, level, game) -> None:
        Family().__init__(address)
        School().__init__(id, level)
        Sports().__init__(game)
