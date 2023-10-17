class Shopping:
    cart = []

    def __init__(self) -> None:
        self.name = "Jamuna"
        self.location = "Bisso road"

    @staticmethod
    def purchase(item, price, amount):
        remaining = amount - price
        print("Buying", item, "Price", remaining)


Shopping.purchase("Cricket kit", 2000, 15000)
