'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.18 (**) Extract a slice from a list.
Given two indices, I and K, the slice is the list containing the elements between the I'th and K'th element of the original list (both limits included). Start counting the elements with 1.

Example:
?- slice([a,b,c,d,e,f,g,h,i,k],3,7,L).
X = [c,d,e,f,g]

Carl James' solution in Python 3.5.1 is below
'''

my_list = ['a','b','c','d','e','f','g','h','i','k']
result = my_list[2:7]

print(result)

try:
    assert result == ['c','d','e','f','g']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

