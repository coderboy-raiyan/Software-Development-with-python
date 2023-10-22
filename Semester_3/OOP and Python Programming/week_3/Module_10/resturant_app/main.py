from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from users import Chef, Customer, Server, Manager
from order import Order


def main():
    menu = Menu()
    pizza_1 = Pizza("Shutki Pizza", 600, "large", ["shutki", "onion"])
    pizza_2 = Pizza("Alur Pizza", 400, "large", ["potato", "onion", "oil"])
    pizza_3 = Pizza("Dal Pizza", 500, "large", ["Dal", "onion", "oil"])
    menu.add_menu_items("pizza", pizza_1)
    menu.add_menu_items("pizza", pizza_2)
    menu.add_menu_items("pizza", pizza_3)

    burger_1 = Burger("Naga Burger", 1000, "chicken", ["bread", "chili"])
    burger_2 = Burger("Beef Burger", 1200, "beef", ["goru", "chili"])
    menu.add_menu_items("burger", burger_1)
    menu.add_menu_items("burger", burger_2)

    coke = Drinks("Coke", 50, True)
    coffee = Drinks("Coffee", 250, False)
    menu.add_menu_items("drinks", coke)
    menu.add_menu_items("drinks", coffee)

    shabnam_blu = Restaurant("Shabnam blu", 1000, menu)
    manager = Manager("KL Rahul", 1500, "January 2020 1",
                      "core team", "8787098", "Mumbai", "klrahul@gmail.com")

    chef = Chef("Rustom Pasha", 3500, "february 2020", "chef",
                "8798123", "DOHS, Mirpur", "rustom@gmail.com", "every")

    server = Server("Chuto", 600, "february 2020", "server",
                    "8798123", "DOHS, Mirpur", "chotu@gmail.com")

    shabnam_blu.add_Employee("manager", manager)
    shabnam_blu.add_Employee("chef", chef)
    shabnam_blu.add_Employee("server", server)

    shabnam_blu.show_employees()

    # Customer - 1
    customer_1 = Customer("King khan", 87432984,
                          "king@khan.com", "Mannat, Mumbai", 200000)

    # Order
    order_1 = Order(customer_1, [pizza_2, coffee])

    # pay order
    customer_1.place_order(order_1)
    shabnam_blu.add_orders(order_1)

    # pay for the order
    shabnam_blu.receive_payment(order_1, 3000, customer_1)

    print("After Customer - 1", shabnam_blu.revenue, shabnam_blu.balance)

    # Customer - 2
    customer_2 = Customer("Salman khan", 87432984,
                          "salman@khan.com", "Mannat, Mumbai", 100000)

    # Order
    order_2 = Order(customer_2, [pizza_3, coke, pizza_1])

    # pay order
    customer_2.place_order(order_2)
    shabnam_blu.add_orders(order_2)

    # pay for the order
    shabnam_blu.receive_payment(order_2, 3000, customer_2)

    print("After Customer - 2", shabnam_blu.revenue, shabnam_blu.balance)

    # pay rent
    shabnam_blu.pay_expense(shabnam_blu.rent,  "Rent")
    shabnam_blu.pay_salary(server)
    print("After Paying rent", shabnam_blu.revenue,
          shabnam_blu.balance, shabnam_blu.expense)


if __name__ == "__main__":
    main()
