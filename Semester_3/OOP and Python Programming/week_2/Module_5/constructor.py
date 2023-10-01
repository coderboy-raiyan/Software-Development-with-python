class Phone:

    def __init__(self, price, brand, color):
        self.price = price
        self.brand = brand
        self.color = color

    def call(self):
        print("calling one person", self.color)

    def send_sms(self, phone, sms):
        text = f"sending SMS to: {phone} and message {sms}"
        self.call()
        return text


my_phone = Phone(2300, "Xiaomi", "Dark")
print(my_phone.price)
my_phone.call()
print(my_phone.send_sms(289092, "I miss u"))
