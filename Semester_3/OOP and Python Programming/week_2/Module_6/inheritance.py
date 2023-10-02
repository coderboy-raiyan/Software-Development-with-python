class Gadgets:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f"Running Laptop : {self.brand}"


class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f"Learning python and practicing"


class Phone (Gadgets):
    def __init__(self, dual_sim, brand, price, color, origin):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)

    def sendMessage(self, number, text):
        return f"Sending SMS to : {number} with : {text}"

    def __repr__(self):
        return f"Phone : Brand - {self.brand} || Color - {self.color} || Dual Sim - {self.dual_sim} || Made in - {self.origin}"


my_phone = Phone(True, "IPhone 15 pro max", 200000, "Dark blue", "China")
print(my_phone)
