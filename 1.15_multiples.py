'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.15 (**) Duplicate the elements of a list a given number of times.
Example:
?- dupli([a,b,c],3,X).
X = [a,a,a,b,b,b,c,c,c]

Prolog problem is above

Carl James' solution in Python 3.5.1 is below
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

