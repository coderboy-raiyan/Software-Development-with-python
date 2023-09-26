
def doubled(num): return num * 2


def add(num1, num2): return num1 + num2


# print(add(10, 20))

numbers = [10, 78, 90]
doubled_nums = map(doubled, numbers)
print(list(doubled_nums))

actors = [
    {"name": "Sabila noor", "age": 28},
    {"name": "Sara Ali Khan", "age": 25},
    {"name": "Mehzabin", "age": 24},
    {"name": "Tara Sutaria", "age": 28},
    {"name": "K kapoor", "age": 45},
    {"name": "Sonam kapoor", "age": 40},
]

younger_artist = filter(lambda actress: actress["age"] < 30, actors)

print(list(younger_artist))
