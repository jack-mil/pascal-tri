# pascal
![image](https://img.shields.io/badge/code%20style-black-000000.svg)
#### Requires *Python 3.9* (type hints)

Module for generating and printing Pascal's Triangle.


Explicit implementation of Pascal's Triangle algorithm. Each row can be generated separately from all others. This vastly speeds up time if all you need is row 100 for example.  
This module is intended to be useful for mathematics or anytime a row(s) of Pascal's triangle might be useful. 

> Includes methods for 
> * generating a list of triangle rows
> * pretty printing a triangle with correct spacing and alignment

The pascal module defines the following methods::

    - To generate a explicit row 'n' of Pascal's triangle:
        calculate_row(n:int) -> list

    - To generate a list of 'n' rows:
        pascal(n:int) -> list (of lists)

    - Pretty print to stdout a triangle with 'n' rows or (optionally) a supplied triangle:
        print_pascal(n:int, triangle=None) -> None
    
Can be run as a script as well.

    pascal.py [-h] [-l LINES]
    If LINES not specified, runs in interactive loop
