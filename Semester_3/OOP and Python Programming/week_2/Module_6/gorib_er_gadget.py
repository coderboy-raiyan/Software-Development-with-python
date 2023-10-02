class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        pass

    def run(self):
        return f"Running Laptop : {self.brand}"

    def coding(self):
        return f"Learning python and practicing"


class Phone:
    def __init__(self):
        pass
