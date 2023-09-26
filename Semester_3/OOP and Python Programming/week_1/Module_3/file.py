with open("message.txt", "a") as file:
    file.write(" I love Macbook pro ")

with open("message.txt", "r") as file:
    text = file.read()
    print(text)
