'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.05 (*) Reverse a list.

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c','d','e','f','g','h','i','j']

result = []
for i in range(1, len(my_list) + 1):
    result.append(my_list[ 0 - i ])

print(result)

try:
    assert result == ['j','i','h','g','f','e','d','c','b','a']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')
