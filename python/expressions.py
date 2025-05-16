"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    return 2 + 19 // 5 - (2- 38)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    # print(2 > 3)

    from datetime import date
    a = date(2025, 1, 1)
    b = date.today()
    c = date(1957, 7, 6)
    d = date.today()
    # print(a == b)
    # print(b == d)
    # print(b is d)
    # print(id(b))
    # print(id(d))
    # print(a > b)

    # print(type(None))
    # print(None > a)
    # print(a == None)

    a = 'Ringo'
    b = 'Ringo'
    print(a == b)
    print(a is b)


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    # print((1 > 2) and (3 < 4))
    # print(1 and 4)
    # print(1 and [4, 3])
    # print(None or [4, 3])

    from datetime import date
    a = date(2025, 1, 1)
    b = date.today()

    print(None or a)
    print(None or None)
    print(a > None)

#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

