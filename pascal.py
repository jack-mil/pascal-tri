# Author: Jackson Miller
# https://github.com/jack-mil/pascal

u"""
Module for generating and printing Pascal's Triangle.

    Includes methods for 
    - generating a list of triangle rows
    - pretty printing a triangle with correct spacing and alignment

The pascal module defines the following methods::

    - To generate a standalone row 'n' of Pascal's triangle:
        calculate_row(n:int) -> list

    - To generate a list of 'n' rows:
        pascal(n:int) -> list (of lists)

    - Pretty print to stdout a triangle with 'n' rows or (optionally) a supplied triangle:
        print_pascal(n:int, triangle=None) -> None
    
Can be run as a script as well. 
- As a script: pascal.py [-h] [-l LINES]
If LINES not specified, runs in interactive loop

"""


__version__ = 1.1


def calculate_row(n: int) -> list:
    """Calculate row 'n' of Pascal's triangle and return a list (0-indexed)."""
    line = [1]
    for k in range(1, n+1):
        # Formula for element k in row n of Pascal's triangle
        value = line[k - 1] * (n + 1 - k) // k
        line.append(value)
    return line


def pascal(rows: int) -> list:
    """Calculate Pascal's triange with the specified number of lines and return a list of rows"""
    return [calculate_row(row) for row in range(rows)]


def print_pascal(lines: int, triangle=None) -> None:
    """Pretty print Pascal's triangle with the specified number of lines.

    - lines -- truncated to an integer. BEWARE: Many lines can be messy 

    - Optionally, provide a triangle to be formatted and printed."""

    if lines == 0:
        print()
        return

    if triangle == None:
        triangle = pascal(lines)

    last_row = triangle[-1]

    # Padding between each element
    max_num_width = len(str(last_row[len(last_row) // 2]))

    # Utility function to format one row of the triangle
    def format_row(row):
        line_str = " ".join([f"{element:^{max_num_width}}" for element in row])
        return line_str

    max_width = len(format_row(last_row))

    # Finally, print each row
    for row in range(lines):
        f_row = format_row(triangle[row])
        # Center the formated row in the space of longest row
        print(f"{f_row:^{max_width}}")


# execute only if run as a script
if __name__ == "__main__":
    import os
    import argparse as argp

    parser = argp.ArgumentParser(description=__doc__)
    parser.add_argument("-l", "--lines",
                        help="The number of lines to print", type=int)
    args = parser.parse_args()

    if args.lines != None:
        print_pascal(args.lines)
    else:
        while True:  # Emulate do_while loop
            lines = input("Number of lines: ")

            try:
                print_pascal(int(lines))
            except ValueError:
                print("Please enter an integer.")

            response = input(
                "\n...press enter to continue.... type 'stop' to exit\n")
            if response == "stop":
                break

            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')
