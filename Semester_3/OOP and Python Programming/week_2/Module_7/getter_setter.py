class Bank:
    def __init__(self, amount) -> None:
        self.__amount = amount

    @property
    def check_amount(self):
        return self.__amount

    @check_amount.setter
    def deposit(self, amount):
        self.__amount += amount


amr_bank = Bank(100000)
amr_bank.deposit = 200
print(amr_bank.check_amount)
