"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Don\'t Pass Me By'
year = 1968

john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]


#%%
# def demonstrate_annotations(title, year):
def demonstrate_annotations(title: str, year: int) -> str:
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """

    print(f'title: {title}, year: {year}')
    print(f'demonstrate_annotations.__annotations__: {demonstrate_annotations.__annotations__}')
    print(f'demonstrate_annotations.__name__: {demonstrate_annotations.__name__}')
    print(f'demonstrate_annotations.__doc__: {demonstrate_annotations.__doc__}')
    return f'demonstrate_annotations("{title}", {year})'


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
def show_song(title, author=ringo, year: int = 1968):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """

    # a = 1
    print(locals())
    print(f'show_song("{title}", {author}, {year})')


#%%
# Test def show_song(title, author=ringo, year: int = 1968):
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """

    # print(members)

    b = band
    b = b + ': ' if members else b
    m = ', '.join(members) if members else ''

    print(f'{b}{m}')


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Beatles', *the_beatles)
use_flexible_arg_list('The Beatles')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    # print(details)
    # print(*details)
    # # print(**details)

    b = band
    # b = b + ': ' if members else b
    m = ', '.join(members) if members else ''
    m = m + '; ' if members else m
    a = 'active' if is_active else 'not active'
    a = a + '; ' if details else a
    d = f'{', '.join([str(k) + ': ' + str(v) for k, v in details.items()])}'

    print(f'{b}: {m}{a}{d}')


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('The Beatles', is_active=False, start=1962, end=1970)
use_all_categories_of_args('The Beatles', *the_beatles, is_active=False,
                           start=1962, end=1970)
