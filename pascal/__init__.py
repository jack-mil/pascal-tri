#!/usr/bin/env python3
# Author: Jackson Miller
# https://github.com/jack-mil/pascal

"""
Module for generating and printing Pascal's Triangle.

    Includes methods for
    - generating a list of triangle rows
    - pretty printing a triangle with correct spacing and alignment

The pascal module defines the following methods::

    - To generate a standalone row 'n' of Pascal's triangle:
        calculate_row(n: int) -> PascalRow

    - To generate a list of 'n' rows:
        pascal(n: int) -> PascalTriangle

    - Pretty print to stdout a triangle with 'n' rows or (optionally) a supplied triangle:
        print_pascal(n: int, triangle: PascalTriangle = None) -> None

Also defined are some type aliases::

    - PascalRow = list[int]
    - PascalTriangle = list[PascalRow]
"""


PascalRow = list[int]
PascalTriangle = list[PascalRow]


def calculate_row(n: int) -> PascalRow:
    """Calculate row 'n' of Pascal's triangle and return a list (0-indexed)."""
    line = [1]
    for k in range(1, n + 1):
        # Formula for element k in row n of Pascal's triangle
        value = line[k - 1] * (n + 1 - k) // k
        line.append(value)
    return line


def pascal(rows: int) -> PascalTriangle:
    """Calculate Pascal's triange with the specified number of lines and return a list of rows"""
    return [calculate_row(row) for row in range(rows)]


def print_pascal(lines: int, triangle: PascalTriangle = None) -> None:
    """Pretty print Pascal's triangle with the specified number of lines.

    - lines -- truncated to an integer. BEWARE: Too many lines can be messy

    - Optionally, provide a triangle to be formatted and printed."""

    if lines == 0:
        print()
        return

    if triangle is None:
        triangle = pascal(lines)

    last_row = triangle[-1]

    # Padding between each element
    largest_num_size = len(str(last_row[len(last_row) // 2]))

    # Utility function to format one row of the triangle
    def format_row(row: PascalRow) -> str:
        return " ".join([f"{element:^{largest_num_size}}" for element in row])

    max_width = len(format_row(last_row))

    # Finally, print each row
    for row in triangle:
        f_row = format_row(row)
        # Center the formated row in the space of longest row
        print(f"{f_row:^{max_width}}")


def version() -> str:
    """
    Get the version of the package installed via pip
    """
    from importlib import metadata

    return metadata.version("pascal-triangle")
