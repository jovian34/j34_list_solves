'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.06 (*) Find out whether a list is a palindrome.
A palindrome can be read forward or backward; e.g. [x,a,m,a,x].

Carl James' solution in Python 3.5.1 is below
'''

def even_palindrome(my_list):
    length_list = int((len(my_list))/ 2)
    for i in range(length_list):
        if my_list[i] != my_list[ 0 - (i+1) ]:
            return False
    return True

def odd_palindrome(my_list):
    length_list = int(((len(my_list)) - 1) / 2)
    for i in range(length_list):
        if my_list[i] != my_list[ 0 - (i+1) ]:
            return False
    return True


my_list = ['a','b','c','d','e','e','d','c','b','a']

if len(my_list) % 2 == 0:
    result = even_palindrome(my_list)
else:
    result = odd_palindrome(my_list)

print(result)

try:
    assert result == True
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')


my_list = ['a','b','c','d','e','d','c','b','a']

if len(my_list) % 2 == 0:
    result = even_palindrome(my_list)
else:
    result = odd_palindrome(my_list)

print(result)

try:
    assert result == True
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')


my_list = ['a','b','f','d','e','e','d','c','b','a']

if len(my_list) % 2 == 0:
    result = even_palindrome(my_list)
else:
    result = odd_palindrome(my_list)

print(result)

try:
    assert result == False
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

