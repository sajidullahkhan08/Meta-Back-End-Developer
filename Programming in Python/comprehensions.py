# List Comprehensions
s = [x**2 for x in range(10)]
print(s) ## Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Dictionary Comprehensions
d = {x: x**2 for x in range(10)}
print(d) ## Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# Set Comprehensions
s2 = {x**2 for x in range(10)}
print(s2) ## Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# Generator Expressions
g = (x**2 for x in range(10))
print(g) ## Output: <generator object <genexpr> at 0x...>
# Converting generator to list to print values
print(list(g)) ## Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# List Comprehensions with conditions
s3 = [x**2 for x in range(10) if x % 2 == 0]
print(s3) ## Output: [0, 4, 16, 36, 64]
# Nested List Comprehensions
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix) ## Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# Flattening a nested list using list comprehension
nested_list = [[1, 2, 3], [4, 5], [6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list) ## Output: [1, 2, 3, 4, 5, 6]
# Using comprehensions with functions
def square(x):
    return x * x
squared_list = [square(x) for x in range(10)]
print(squared_list) ## Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Using comprehensions with string methods
words = ["hello", "world", "python"]
capitalized_words = [word.upper() for word in words]
print(capitalized_words) ## Output: ['HELLO', 'WORLD', 'PYTHON']
# Combining two lists into a dictionary using comprehensions
keys = ['a', 'b', 'c']
values = [1, 2, 3]
combined_dict = {k: v for k, v in zip(keys, values)}
print(combined_dict) ## Output: {'a': 1, 'b': 2, 'c': 3}
# Filtering a list using comprehensions
filtered_list = [x for x in range(20) if x % 3 == 0]
print(filtered_list) ## Output: [0, 3, 6, 9, 12, 15, 18]
# Using comprehensions to create a list of tuples
tuples_list = [(x, x**2) for x in range(5)]
print(tuples_list) ## Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
# Using comprehensions to create a list of even numbers
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers) ## Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Using comprehensions to create a list of odd numbers
odd_numbers = [x for x in range(20) if x % 2 != 0]
print(odd_numbers) ## Output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]