# This code demonstrates how to handle exceptions in Python.
items = [1,2,3,4,5]
try:
    item = items[6]
    print(item)
except Exception as e:
    print("Item does not exist in the list..!", e)

# Division by zero example
def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40, 0)
    print(ans)
except ZeroDivisionError as e:
    print(0, "Zero cannot be used as a divisor", e)

# File handling example
# Attempting to read a file that does not exist
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found..")