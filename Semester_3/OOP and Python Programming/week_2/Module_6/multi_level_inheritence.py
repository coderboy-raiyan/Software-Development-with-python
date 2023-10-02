class Vehicle:
    def __init__(self, type, engine, model, seats) -> None:
        self.type = type
        self.engine = engine
        self.model = model
        self.seats = seats


class Bus(Vehicle):
    def __init__(self, type, engine, model, seats, weight) -> None:
        self.weight = weight
        super().__init__(type, engine, model, seats)


class Truck(Bus):
    def __init__(self, type, engine, model, seats, weight) -> None:
        super().__init__(type, engine, model, seats, weight)
