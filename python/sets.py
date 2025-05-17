"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    the_beatles = set()
    print(the_beatles)
    the_beatles = {'John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr'}
    print(the_beatles)
    the_beatles.add('Ringo')
    print(the_beatles)
    the_beatles.remove('Ringo')
    print(the_beatles)
    the_beatles.add('Ringo Starr')
    print(the_beatles)

    the_beatles = ['John Lennon', 'Paul McCartney', 'George Harrison', 'Ringo Starr', 'Ringo Starr']
    print(the_beatles)
    the_beatles = list(set(the_beatles))
    print(the_beatles)

    print({'John Lennon', 'Paul McCartney', 'George Harrison', } & {'George Harrison', 'Ringo Starr', })
    print({'John Lennon', 'Paul McCartney', 'George Harrison', } | {'George Harrison', 'Ringo Starr', })
    print({'John Lennon', 'Paul McCartney', 'George Harrison', } ^ {'George Harrison', 'Ringo Starr', })
    print({'John Lennon', 'Paul McCartney', 'George Harrison', } - {'George Harrison', 'Ringo Starr', })


#%%
# Test demonstrate_sets()
demonstrate_sets()


