'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.17 (*) Split a list into two parts; the length of the first part is given.
Do not use any predefined predicates.

Example:
?- split([a,b,c,d,e,f,g,h,i,k],3,L1,L2).
L1 = [a,b,c]
L2 = [d,e,f,g,h,i,k]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c','d','e','f','g','h','i','k']
result_1 = my_list[:3]
result_2 = my_list[3:]

print(result_1)
print(result_2)

try:
    assert result_1 == ['a', 'b', 'c']
    assert result_2 == ['d','e','f','g','h','i','k']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

