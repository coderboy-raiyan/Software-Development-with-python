class Phone:
    price = 20000
    color = 'Red'
    brand = "Iphone"
    features = ["camera", "speaker"]

    def call(self):
        print("calling one person")

    def send_sms(self, phone, sms):
        text = f"sending SMS to: {phone} and message {sms}"
        return text


my_phone = Phone()
print(my_phone.price)
my_phone.call()
print(my_phone.send_sms(289092, "I miss u"))
