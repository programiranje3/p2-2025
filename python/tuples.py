"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    # ringo = ()
    # print(ringo)
    # ringo = ('Ringo Starr', )
    # print(ringo)
    # ringo = 'Ringo Starr',
    # print(ringo)
    # ringo = 'Ringo Starr', 1940
    ringo = 'Ringo Starr', 1940, 'Liverpool'
    print(ringo)
    print(ringo[-1])

    # ringo[-1] = 1940


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    the_beatles = 'John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr',
    print(the_beatles)
    john, paul, george, ringo = the_beatles
    print(john, paul, george, ringo)
    # print(john, paul, george, ringo, sep=', ')
    print(', '.join(the_beatles))
    print(list(the_beatles))


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr', )
    birth_years = (1940, 1942, 1943, 1940)
    birth_places = ('Liverpool', 'Liverpool', 'Liverpool', 'Liverpool' )

    the_beatles_zip = zip(members, birth_years, birth_places)
    print(the_beatles_zip)
    # print(list(the_beatles_zip))
    # print(list(zip(members, birth_years, birth_places)))
    for member, birth_year, birth_place in the_beatles_zip:
        print(member, birth_year, birth_place, sep=', ')
    # print(list(the_beatles_zip))
    print(list(zip(members, birth_years, birth_places)))


#%%
# Test demonstrate_zip
demonstrate_zip()

