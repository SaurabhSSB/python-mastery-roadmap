"""
This script demonstrates various input and output operations in Python, including type-specific inputs,
multiple outputs, comments, variables, data types, and escape sequence usage.
"""

def main() -> None:
    """
    Main function to execute the input-output demonstration.
    """
    # Variables are like containers that hold data.
    # Variables can be updated, meaning they are dynamic, not static.
    a1: int = 1
    B1: int = 2
    _c1: int = 3
    # Note: Variable names cannot start with numbers, e.g., 1c_ = 4 would cause an error.

    print(a1, B1, _c1)  # Print the values of variables
    print("This is type of a1", type(a1))  # Print the type of variable `a1`

    # Data type specifies the type of value a variable holds.
    '''
    5 types of data types:
    1. Numeric: int, float, complex
    2. String
    3. Boolean: True, False
    4. Sequenced: list- [], tuple- () -> list is mutable (can be modified) and tuple is immutable (cannot be modified)
    5. Mapped: dictionary
    '''
    print("Numeric Data Type= ", 3, " ", 7.83, " ", 6+2j)  # Demonstrating int, float, and complex types
    print("String Data Type= ", "This is Python String", 'And we are learning Programming')  # String example
    print("Boolean Data Type= ", True)  # Boolean example
    print("Sequenced Data Type= ", [12, 15, 16, 18], " ", (11, 14, 17, 19))  # List and tuple examples
    print("Dictionary= ", {"name": "Rohan", "age": 25, "Student": True, "Stream": "MBA"})  # Dictionary example

    # Explicit typecasting - Done by user
    string: str = "15"
    number: int = 7
    string_number: int = int(string)  # Throws an error if the string is not a valid integer
    sum_result: int = number + string_number
    print("The Sum of both the numbers is: ", sum_result)  # Print the sum of explicitly casted values

    # Implicit typecasting - Done by Python automatically
    a: int = 7  # Python treats `a` as an integer
    print(type(a))  # Print type of `a`

    b: float = 3.0  # Python treats `b` as a float
    print(type(b))  # Print type of `b`

    c: float = a + b  # Python automatically converts `a` to float during addition
    print(c)  # Print the result of implicit typecasting
    print(type(c))  # Print type of `c`

    # Global and Local Variables
    # Variables defined inside a function body have a local scope, and those defined outside have a global scope.

    a: int = 1  # Global variable

    def x1() -> None:
        print('Inside x1(): ', a)  # Accessing global variable `a`

    def x2() -> None:
        a: int = 2  # Local variable
        print('Inside x2(): ', a)  # Here `a` = 2 using the local `a`

    def x3() -> None:
        global a
        a = 3  # Modifying the global variable
        print('Inside x3(): ', a)  # Here `a` = 3 using global `a` because of the `global` keyword

    print('global: ', a)  # Print initial value of global variable `a`
    x1()
    print('global: ', a)  # Global `a` remains unchanged
    x2()
    print('global: ', a)  # Global `a` remains unchanged
    x3()
    print('global: ', a)  # Value of global `a` changes due to `x3`

if __name__ == "__main__":
    main()
