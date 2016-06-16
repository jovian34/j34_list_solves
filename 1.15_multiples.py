'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.15 (**) Duplicate the elements of a list a given number of times.
Example:
?- dupli([a,b,c],3,X).
X = [a,a,a,b,b,b,c,c,c]


A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c']
result = []

for letter in my_list:
    for i in range(3):
        result.append(letter)
print(result)

try:
    assert result == ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

