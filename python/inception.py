"""The very first module in a more structured version of the project.
"""


#%%
# Moving part of the code from main.py


#%%
# Printing with ' ' and printing without '\n'
# print('Ringo Starr')
# print('Ringo Starr' + '\nJohn Lennon', )
# print(__name__)


#%%
# A simple function and function call
def print_ringo():

    """This is the docstring of print_ringo().
    """

    print('Ringo Starr')
    print('Yeah!')

# print_ringo()
# print(__name__)


#%%
# Printing docstrings


#%%
# break and continue
for i in range(1, 5):
    if i == 3:
        # continue
        break
    print(i)

#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes
from datetime import date
from settings import *
d = date(2025, 1, 1)
print(d.strftime(PREFERRED_DATE_FORMAT))

#%%
# Testing print(__file__)


#%%
# Taking care of the module __name__
if __name__ == '__main__':
    print(__name__)
    print(print_ringo.__doc__)
    # print_ringo()

