"""Demonstrates functions as parameters of other functions,
functions as return values of other functions and
user-defined decorators
"""


#%%
# Setup / Data

import functools

from python.functions import *

# Setup / Data
john = 'John Lennon'
paul = 'Paul McCartney'
george = 'George Harrison'
ringo = 'Ringo Starr'
the_beatles = [john, paul, george, ringo]


#%%
def pass_simple_function_as_parameter():
    """Demonstrates using another function as a parameter. It works because functions are objects.
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f.
    """

    # Try something like this in Python Console:
    #     p = *[1,2,3]        # generates an error;
    #                           asterisk * isn't simply unary operator,
    #                           it's argument-unpacking operator for function definitions and function calls;
    #                           heuristics: use it "inside of something else", like inside (), [] and constructors
    #     p = *[1,2,3],       # generates a tuple, because of the comma (* is actually "inside creating a tuple")
    #     p = 44, *[1,2,3]    # generates another tuple
    #     print(p)
    #     print(*p)

    # Case 1: 0 or more arguments

    # Try also this in Python Console:
    #     def f(*args):
    #         return sum(args)      # it must be sum(args), not sum(*args); e.g. in Python Console sum((1, 2)) is OK
    #     def g(f, *args):
    #         return f(*args)       # heuristics: if *args is in a f. signature, use *args in the f. body as well
    #     g(f, *(1, 2, 3))          # result: 6
    #     g(f, *[1, 2, 3])          # result: 6

    # Case 2: 1 or more arguments (the first one is positional)


#%%
# Test pass_simple_function_as_parameter()
pass_simple_function_as_parameter()


#%%
def pass_function_as_parameter(f, *args, **kwargs):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    The argument/parameter list specified as in this function is a fairly general one -
    it works regardless of the number of *args and **kwargs in the function call (both can be 0).
    However, if f includes positional arguments, they must be passed in the call to this function.
    In that case, they are treated as part of the *args argument of this function,
    but must be passed explicitly in the call to this function.
    Optional *args of f may or may not be passed in the call to this function (just like in the call to f).
    Likewise, if f is called with default arguments,
    they are included in the **kwargs argument of this function.
    In other words, from https://stackoverflow.com/a/3394898/1899061:
    You can use *args and **kwargs along with named arguments too. The explicit arguments get values first
    and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:
        def table_things(titlestring, **kwargs)
    If f has default arguments, they can be included in **kwargs in the beginning of f
    (e.g., if f has a default arg d=4, then the first line of f would be kwargs['d'] = d),
    and then f is called as f(*args, **kwargs), just as if d=4 was always part of **kwargs:
    -------
    def f(*args, year=2004, **kwargs):
        kwargs['year'] = year

        print(args)             # result: a tuple of args
        print(*args)            # result: a sequence of args, 'untupled'
        print(kwargs)

    def g(h, *args, **kwargs):
        return h(*args, **kwargs)

    g(f, 'Ringo', 'Starr', True, birth=1940)
    -------
    See https://stackoverflow.com/a/34206138/1899061 for further details.
    """


#%%
# Test pass_function_as_parameter(f, *args, **kwargs)
pass_function_as_parameter(use_all_categories_of_args, 'The Beatles', *the_beatles, is_active=False,
                           start=1962, end=1970)


#%%
def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """


#%%
# Test return_function(full_name, first_name_flag)
# f = return_function('Ringo Starr', False)
# print(f())


#%%
def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty tuple (or an empty list)
    - a function that returns a tuple of args (or a list of args, or...)
    """


#%%
# Test return_function_with_args(*args)
# f = return_function_with_args()
# f = return_function_with_args(1)
# print(f('Ringo', 'Starr', 1940))


#%%
def a_very_simple_decorator(f):
    """Illustrates the essential idea of decorators:
        - take a function (f) as a parameter of a decorator function (decorator)
        - use the parameter function f inside an inner wrapper function (g)
        - return the inner wrapper function g from the decorator function
    Then define f and run f = decorator(f) before calling f.
    Even better, just put @decorator before the definition of f. Each call to f will then actually run decorator(f).
    """

    # Examples (run them in Python Console):

    # def decorator(f):
    #     def g():
    #         return f('Ringo Starr')
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something)
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Ringo Starr

    # def decorator(f, *args):
    #     def g():
    #         print('Ringo Starr')
    #         return f(*args)
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something, 'Ringo Starr')
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Ringo Starr
    # Ringo Starr


#%%
# Test a_very_simple_decorator(f)
def songs(*args):
    print(f'{", ".join([arg for arg in args])}')


#%%
songs('Act Naturally', 'With a Little Help from My Friends')

#%%
# f = a_very_simple_decorator(songs)
# f('Act Naturally', 'With a Little Help from My Friends')

#%%
# songs = a_very_simple_decorator(songs)
# songs('Act Naturally', 'With a Little Help from My Friends')
# print()
# songs()


#%%
def band_details(f_to_decorate):
    """Demonstrates how to develop a decorator.
    Uses the decorator-writing pattern (https://stackoverflow.com/a/3394911/1899061):
    import functools
    def decorator(f_to_decorate):
        @functools.wraps(f_to_decorate)			        # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):         # see https://stackoverflow.com/a/309000/1899061 for details
            # Do something before
            value = f_to_decorate(*args, **kwargs)      # (*args, **kwargs) are wrapper_decorator's formal arguments!
            # Do something after
            return value
        return wrapper_decorator
    """


#%%
@band_details
def print_band(name, *members, **years_active):
    """If not decorated, just prints the name a band, assuming that the name is a string.
    The decorator before the function signature (@members) illustrates how to apply a decorator;
    omit it if decorating manually.
    """


#%%
# Test members(f_to_decorate)
print_band('The Beatles', *the_beatles, )
print_band('The Beatles', start=1962, end=1970)
print_band('The Beatles', *the_beatles, start=1962, end=1970)

#%%
# Demonstrating the purpose of @functools.wraps(f_to_decorate)
print(print_band.__name__)      # try it with and without @functools.wraps(f_to_decorate) in the decorator

