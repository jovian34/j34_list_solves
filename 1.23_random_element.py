'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.23 (**) Extract a given number of randomly selected elements from a list.
The selected items shall be put into a result list.
Example:
?- rnd_select([a,b,c,d,e,f,g,h],3,L).
L = [e,d,a]

Prolog problem is above

Carl James' solution on Python 3.5.1 is below
'''

import random

def random_element(start_list, select):
    temp_list = []
    for element in start_list:
        temp_list.append(element)
    result_list = []
    for i in range(select):
        index = random.randint(0, len(temp_list)-1 )
        remove = temp_list[index]
        result_list.append(temp_list[i])
        temp_list.remove(temp_list[i])
    print(temp_list)
    print(start_list)
    return result_list

start_list = ['a','b','c','d','e','f','g','h']
select = 3
result = random_element(start_list, select)
print(result)

try:
    assert len(result) == 3
    for letter in result:
        print(letter)
        assert letter in start_list
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

