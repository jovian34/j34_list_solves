'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.14 (*) Duplicate the elements of a list.
Example:
?- dupli([a,b,c,c,d],X).
X = [a,a,b,b,c,c,c,c,d,d]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c','c','d']
result = []

for letter in my_list:
    for i in range(2):
        result.append(letter)
print(result)

try:
    assert result == ['a','a','b','b','c','c','c','c','d','d']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

