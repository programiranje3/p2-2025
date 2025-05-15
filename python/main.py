"""The very first Python script - main.py.
"""

# #%%
# # Hello world: the print() built-in function and the + operator.
# print('Ringo Starr')
# print('Ringo Starr' + '\nJohn Lennon', )
#
#
# #%%
# # The input() built-in function
# # print('Prompt: ')
# # ringo = input()
# # print(ringo)
# print(input('Prompt: '))
#
#
# #%%
# # A simple function and function call
# def print_ringo():
#     print('Ringo Starr')
#     print('Yeah!')
#
#
# #%%
# print_ringo()
#
#
# #%%
# # A simple loop and the range() built-in function
# for i in range(1, 5):
#     print(i)
#
#
# #%%
# # A simple list, accessing list elements, printing lists
# the_beatles = ['John', 'Paul', 'George', 'Ringo']
# print(the_beatles)
# print(the_beatles[2])
#
#
# #%%
# # Looping through list elements - for and enumerate()
# # for musician in the_beatles:
# #     print(musician)
# for i, musician in enumerate(the_beatles):
#     print(i+1, musician)
# print(enumerate(the_beatles))


# #%%
#
# """Doc string of this cell.
# """
#
# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# print(__doc__)


#%%
# Importing from another script
from python.inception import print_ringo
print_ringo()

