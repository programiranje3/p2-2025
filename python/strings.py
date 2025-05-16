"""Demonstrates working with strings in Python.
"""


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    # print('This is %d and %s has released a new album.' % (2025, 'Ringo'))
    # print('C:\nobody')
    # print(r'C:\nobody')
    # print("""
    # Ringo
    # Starr
    # """)
    # print('Ringo ' * 3)
    # print('Ringo Starr'[:])
    print(str('\tRingo'))
    print(repr('\tRingo'))


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('Ringo Starr has relead a new {} in {}.'.format('album', '2025'))


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    year = 2025
    product = 'album'
    print(f'Ringo Starr has released a new {product * 3} in {year + 2}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    print('Ringo Starr'.endswith('Starr'))
    print('Ringo Starr'.split('go '))
    print('Ringo Starr'.split())
    print('Ringo Starr'.center(30, '*'))
    print('go' in 'Ringo Starr')
    print(len('Ringo Starr'))
    # print('           Ringo Starr'.strip())
    print('           Ringo Starr'.lstrip())
    print('           Ringo Starr*********'.rstrip('*'))
    # print('           Ringo Starr       '.strip())


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
