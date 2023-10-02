class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposit

    def deposit(self, amount):
        self.__balance += amount

    def get_Balance(self):
        return self.__balance


towhid_afridi = Bank("Towhid afridi", 50000)
towhid_afridi.deposit(4500)
print(towhid_afridi.get_Balance())
