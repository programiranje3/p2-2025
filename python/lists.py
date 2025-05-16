"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    ringo = ['Ringo Starr', 1940, True, 'The Beatles']
    print(ringo)
    print(ringo[1])
    print(ringo[1:3])
    print(ringo[-2:])
    print(ringo == ['Ringo Starr', 1940, True, 'The Beatles'])
    print(ringo is ['Ringo Starr', 1940, True, 'The Beatles'])
    print(ringo + ['John Lennon'])
    print()

    for e in ringo:
        print(e)


#%%
# Test demonstrate_lists()
demonstrate_lists()

#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    ringo = ['Ringo Starr', 1940, True, 'The Beatles']
    print(ringo)
    # print(ringo.append('John Lennon'))
    ringo.append('John Lennon')
    print(ringo)
    ringo.insert(2, 'Paul McCartney')
    print(ringo)
    ringo.remove('Paul McCartney')
    print(ringo)
    ringo.pop()
    print(ringo)
    ringo.extend(['John Lennon', 'Paul McCartney'])
    print(ringo)
    ringo.append('John Lennon')
    print(ringo)
    print(ringo.count('John Lennon'))
    print(ringo.index('John Lennon'))
    ringo.reverse()
    print(ringo)
    print(len(ringo))
    print('John Lennon' in ringo)
    print('John Lennon' not in ringo)


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import seed, randint
    l = []
    seed(3546)
    for i in range(10):
        l.append(randint(1, 100))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    ringo = ['Ringo Starr', 1940, True, 'The Beatles']
    # r = ringo
    # r = ringo.copy()
    # r = ringo + []
    r = ringo[:]
    print(r)
    print(id(r))
    print(id(ringo))


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane', ]

    first_words = [s.split()[0] for s in songs]
    print(first_words)
    # first_letters = [w[0] for w in first_words]
    # first_letters = ''.join([w[0] for w in first_words])
    # first_letters = ''.join([w[0] for w in first_words]).capitalize()
    first_letters = ''.join([w[0] for w in first_words]).capitalize() + '!'
    print(first_letters)

    songs = ['Honey Don\'t', 'Eleanor Rigby', 'Lucy in the Sky With Diamonds', 'Penny Lane', 'Eleanor Rigby', ]
    i = [i for i, title in enumerate(songs) if title == 'Eleanor Rigby']
    print(i)


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

