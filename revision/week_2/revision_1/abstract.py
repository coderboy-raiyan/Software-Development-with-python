from abc import ABC, abstractmethod


class Mechanism(ABC):
    def __init__(self, brand, price) -> None:
        self.brand = brand
        self.price = price

    @abstractmethod
    def drive():
        print("Drive the car")


class Car(Mechanism):
    def __init__(self, brand, price) -> None:
        super().__init__(brand, price)

    def drive():
        print("Drive the car")

    def __repr__(self) -> str:
        return f"{self.brand} : Price - {self.price}"


bmw = Car("BMW X7", 10000000)
# bmw.drive()
print(bmw)
