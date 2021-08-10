# Pascal-Triangle

<div align="center">
<a href="https://pypi.org/project/pascal-tri/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pascal-tri?style=flat-square&label=Python&logo=python&logoColor=yellow"></a>
<a href="https://pypi.org/project/pascal-tri/"> <img alt="PyPi" src="https://img.shields.io/pypi/v/pascal-tri?style=flat-square&label=PyPI&logo=pypi&logoColor=yellow"></a>
<a href="https://pypi.org/project/pascal-tri/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/pascal-tri?style=flat-square&label=Downloads"></a>
<a href="https://github.com/jack-mil/pascal-triangle/blob/master/LICENSE"> <img alt="Github" src="https://img.shields.io/github/license/jack-mil/pascal-triangle?style=flat-square&label=License"></a>
<a href="https://github.com/psf/black"><img alt="Formatting" src="https://img.shields.io/badge/Code%20Style-Black-000000?style=flat-square"></a>
</div>

## Module for generating and printing Pascal's Triangle ##
### Requires *Python 3.9* (type hints) ###

Explicit implementation of Pascal's Triangle algorithm. Each row can be generated separately from all others. This vastly speeds up time if all you need is row 100 for example.
This module is intended to be useful for mathematics or anytime a row(s) of Pascal's triangle might be useful.


### Installation ###
*Pascal-triangle* can be installed directly with pip to use as a library and shell command by running `pip install pascal-tri`

OR clone the repo and run `python -m pascal`


### Includes methods for ###
> * generating a list of triangle rows
> * pretty printing a triangle with correct spacing and alignment

The pascal module defines the following methods, access with
```py
from pascal import *
```
```py
    # To generate a explicit row 'n' of Pascal's triangle:
        calculate_row(n: int) -> PascalRow

    # To generate a list of 'n' rows:
        pascal(n: int) -> PascalTriangle

    # Pretty print to stdout a triangle with 'n' rows or (optionally) a supplied triangle:
        print_pascal(n: int, triangle: PascalTriangle = None) -> None
```
Can be run as a script as well.

    python -m pascal [-h] [-l LINES]
      If LINES not specified, runs in interactive loop


## Learning objectives ##

This project exists as an exercise in learning these techonlogies/concepts
 - Python type hinting (VS code intellisense integration)
 - Making distributable Python packages (PyPi)
 - Github Actions to build/publish automatically