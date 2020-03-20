# pascal
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
  pascal.py [-h] [-l LINES]
If LINES not specified, runs in interactive loop
