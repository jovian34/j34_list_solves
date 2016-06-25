'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.01 (*) Find the last element of a list.
Example:
?- my_last(X,[a,b,c,d]).
X = d

Prolog problem is above

Carl James' solution in Python 3.5.1 is below
'''

my_list = ['a','b','c','d']
last_element = my_list[-1]
print(last_element)

try:
    assert last_element == 'd'
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')
