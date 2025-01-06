"""
This script demonstrates various input and output operations in Python, including type-specific inputs,
multiple outputs, comments, and escape sequence usage.
"""

def main() -> None:
    """
    Main function to execute the input-output demonstration.
    """
    # Input section
    a: str = input("Enter the value: ")  # Prompt user for a string input
    b: int = int(input("Enter an integer value: "))  # Prompt user for an integer input
    c: float = float(input("Enter a float value: "))  # Prompt user for a float input

    # Output section
    print(a)  # Print the string input
    print(b + c)  # Print the sum of integer and float inputs
    print(5 + 2)  # Print a simple arithmetic result
    print("Python")  # Print a string
    print(7, 8.12, "Python", sep="-", end="$\n")  # Print with custom separator and end character

    # Multiple outputs in a single print statement
    print(a, 7, 8, 6 + 5,"S")  # Print mixed values in one line

    # Escape Sequence Character Demonstration
    print("This is for escape sequence\t \" We can use\" symbol too\n Escape Sequence")

if __name__ == "__main__":
    main()
