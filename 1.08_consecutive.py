'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.08 (**) Eliminate consecutive duplicates of list elements.
If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

Example:
?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [a,b,c,a,d,e]

Carl James' solution in Python 3.5.1 is below
'''

my_list = [ 'a', 'a', 'a', 'a', 'b', 'c', 'c', 'a', 'a', 'd', 'e', 'e', 'e', 'e']
result = [ my_list[0] ]
prior_letter = my_list[0]
for i in range(1, len(my_list)):
    if prior_letter != my_list[i]:
            result.append(my_list[i])
    prior_letter = my_list[i]
    
print(result)

try:
    assert result == ['a','b','c','a','d','e']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

