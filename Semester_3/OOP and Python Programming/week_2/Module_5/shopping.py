class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, itemName, price, quantity):
        product = {"name": itemName, "price": price, "quantity": quantity}
        self.cart.append(product)

    def getCart(self):
        return self.cart

    def removeFromCart(self, name):
        self.cart = list(
            filter(lambda item: item.get('name') != name, self.cart))
        print(self.cart)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item["price"]

        if (amount < total):
            print("Please provide with ", total - amount, " more taka")
        else:
            if (amount > total):
                print("Here is your returns ", amount - total)
            print("Payment Successful")

    def __repr__(self):
        return self.name


kartik_aryaan = Shopping("Kartik Aryaan")
kartik_aryaan.add_to_cart("Watch", 8000, 2)
kartik_aryaan.add_to_cart("Shoes", 12000, 1)

kartik_aryaan.checkout(50000)
print(kartik_aryaan)
