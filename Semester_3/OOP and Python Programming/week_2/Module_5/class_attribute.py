class Shop():
    shopName = "Jamuna"  # class attribute

    def __init__(self, buyer):
        self.buyer = buyer  # instance attribute
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


sabila_noor = Shop("Sabila Noor")
sabila_noor.add_to_cart("IPhone 13 pro max")
sabila_noor.add_to_cart("Mac Book pro")
print(sabila_noor.cart)

jovan = Shop("Jovan")
jovan.add_to_cart("glasses")
jovan.add_to_cart("foot ware")
print(jovan.cart)
