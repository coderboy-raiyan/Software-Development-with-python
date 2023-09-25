numbers = [10, 20, 30, 40]

numbers.append(10)
numbers[1] = 0
numbers.insert(2, 999)
numbers.remove(40)
last = numbers.pop()
print(last)
numbers.sort(reverse=True)
print(numbers[:])
