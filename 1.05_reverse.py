'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.05 (*) Reverse a list.

Carl James' solution in Python 3.5.1 is below
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
