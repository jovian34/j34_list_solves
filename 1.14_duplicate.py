'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.14 (*) Duplicate the elements of a list.
Example:
?- dupli([a,b,c,c,d],X).
X = [a,a,b,b,c,c,c,c,d,d]

Carl James' solution in Python 3.5.1 is below
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

