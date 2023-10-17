class Gadgets:
    def __init__(self, brand, color, model, price) -> None:
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price


class Laptop(Gadgets):

    def __init__(self, brand, color, model, price) -> None:
        super().__init__(brand, color, model, price)

    def run(self):
        return f"Running laptop : {self.brand}"


class Phone(Gadgets):
    def __init__(self, brand, color, model, price) -> None:
        super().__init__(brand, color, model, price)

    def run(self):
        return f"Running phone : {self.brand}"


newLaptop = Laptop("Macbook max pro", "Mash", "avenger9", 230000)
newPhone = Phone("Iphone", "Purple", "15", 34000)
newPhone.run()

print(newLaptop.service_center)
