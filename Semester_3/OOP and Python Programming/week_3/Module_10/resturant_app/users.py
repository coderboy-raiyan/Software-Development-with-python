import abc


class User (abc.ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address,  money) -> None:
        super().__init__(name, phone, email, address)
        self.wallet = money
        self.due_bill = 0
        self.__order = None

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_bill += order.bill
        print(f"{self.name} placed an order with bill {order.bill}")

    def eat_food(self, order):
        print(f"{self.name} eating these foods {order.items}")

    def pay_for_order(self, amount):
        pass

    def give_tips(self, amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, salary, starting_date, department, phone, address, email) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department

    def receive_salary(self):
        self.due = 0


class Chef(Employee):
    def __init__(self, name, salary, starting_date, department, phone, address, email, cooking_item) -> None:
        super().__init__(name, salary, starting_date, department, phone, address, email)
        self.cooking_item = cooking_item


class Server(Employee):
    def __init__(self, name, salary, starting_date, department, phone, address, email) -> None:
        super().__init__(name, salary, starting_date, department, phone, address, email)
        self.tips_earing = 0

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self, amount):
        self.tips_earing += amount


class Manager(Employee):
    def __init__(self, name, salary, starting_date, department, phone, address, email) -> None:
        super().__init__(name, salary, starting_date, department, phone, address, email)
