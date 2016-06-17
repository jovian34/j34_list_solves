'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.02 (*) Find the last but one element of a list.
(de: zweitletztes Element, fr: avant-dernier élément)

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.


Prolog problem is above

Carl James' solution is below
'''

my_list = ['a','b','c','d']
last_but_one_element = my_list[-2]
print(last_but_one_element)

try:
    assert last_but_one_element == 'c'
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')
