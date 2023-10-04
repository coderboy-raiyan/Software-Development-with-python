class Shop():
    def __init__(self) -> None:
        self.products = []

    def add_product(self, itemName, price, stock):
        self.products.append(product)

    def update_stock(self, name, quantity):
        for item in self.products:
            if (item["name"] == name and item["stock"] >= quantity):
                item["stock"] -= quantity
                return item

    def buy_product(self, name, quantity):
        findOne = list(
            filter(lambda product: product["name"] == name, self.products))[0]

        if (findOne["stock"] >= quantity):
            item = self.update_stock(name, quantity)
            print("Order successfully done", item)
        else:
            print("Oop! Sorry, this product is not available")

    def __repr__(self) -> str:
        print(self.products)
        return "Operation Done"


class Product(Shop):
    pass
