'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.04 (*) Find the number of elements of a list.

Prolog problem is above

Carl James' solution in Python 3.5.1 is below
'''

my_list = ['a','b','c','d','e','f','g','h','i','j']


result = len(my_list)


print(result)

try:
    assert result == 10
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')
