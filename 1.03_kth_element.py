'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.04 (*) Find the number of elements of a list.

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.

Prolog problem is above

Carl James' solution is below
'''

my_list = ['a','b','c','d','e','f','g','h','i','j']


result = len(my_list)


print(result)

try:
    assert result == 10
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')
