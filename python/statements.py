"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    if 0:
        print('2 > 3')
    elif []:
        print('3 > 5')
    elif 5 == 6:
        print('5 == 6')
    else:
        print('2 < 3')


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    # for i in range(1, 20, 4):
    #     print(i)

    # for _ in range(5):
    #     print('Ringo')

    a = 1
    while a < 10:
        print(a)
        a += 1


#%%
# Test demonstrate_loops()
demonstrate_loops()
