class Engine:
    def __init__(self) -> None:
        pass

    def start():
        return "Engine started"


class Driver:
    def __init__(self) -> None:
        pass


# Car "has a" engine


class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()
