def read_file(file_name):
    """Reads and returns the entire contents of a file as a single string."""
    with open(file_name, 'r') as file:     # Opens file in read mode using context manager
        contents = file.read()             # Reads the full file as one big string
        print(contents)                    # Prints the contents
        return contents                    # Returns it


def read_file_into_list(file_name):
    """Reads a file and returns a list where each element is a line in the file."""
    lines = []                             # Create empty list to store lines
    with open(file_name, 'r') as file:     # Open file
        lines = file.readlines()           # Read all lines into a list (includes '\n')
    return lines


def write_first_line_to_file(file_contents, output_filename):
    """Writes the first line of a string to a given file."""
    first_line = file_contents.split('\n')[0]  # Get everything before the first newline
    with open(output_filename, 'w') as file:   # Open file in write mode
        file.write(first_line)                 # Write first line only


def read_even_numbered_lines(file_name):
    """Reads even-numbered lines of a file and returns them as a list."""
    even_lines = []                              # List to hold even-numbered lines
    with open(file_name, 'r') as file:
        for index, line in enumerate(file, start=1):  # start=1 to match human line numbers
            if index % 2 == 0:
                even_lines.append(line)          # Add even lines (2, 4, 6, etc.)
    return even_lines


def read_file_in_reverse(file_name):
    """Reads a file and returns a list of its lines in reverse order."""
    with open(file_name, 'r') as file:
        lines = file.readlines()                # Read all lines into a list
        reversed_lines = lines[::-1]            # Reverse the list
        print(reversed_lines)                   # Print the reversed lines
        return reversed_lines

def main():
    file_contents = read_file("sampletext.txt")
    print("----- read_file_into_list -----")
    print(read_file_into_list("sampletext.txt"))
    
    print("----- write_first_line_to_file -----")
    write_first_line_to_file(file_contents, "output.txt")
    print("First line written to output.txt")

    print("----- read_even_numbered_lines -----")
    print(read_even_numbered_lines("sampletext.txt"))

    print("----- read_file_in_reverse -----")
    print(read_file_in_reverse("sampletext.txt"))
