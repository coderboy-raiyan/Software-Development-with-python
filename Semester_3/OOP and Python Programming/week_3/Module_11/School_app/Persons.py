import random


class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def tech(self):
        pass

    def take_exam(self, students):
        for student in students:
            marks = random.randint(0, 100)


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.marks = {}
        self.grade = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value
