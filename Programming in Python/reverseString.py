# slicing function for reversing a string
def reverse_string(s):
    return s[::-1] # logic: slicing the string from end to start

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    reversed_string = reverse_string(input_string)
    print("Reversed string:", reversed_string)

# String reversal using recursion
def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

# Example usage of recursive string reversal
if __name__ == "__main__":
    input_string = input("Enter a string to reverse recursively: ")
    reversed_string_recursive = reverse_string_recursive(input_string)
    print("Reversed string (recursive):", reversed_string_recursive)