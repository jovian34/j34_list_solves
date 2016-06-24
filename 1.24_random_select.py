'''
1.24 (*) Lotto: Draw N different random numbers from the set 1..M.
The selected numbers shall be put into a result list.
Example:
?- rnd_select(6,49,L).
L = [23,1,17,33,21,37]

Prolog problem is above

Carl James' solution on Python 3.5.1 is below
'''

import random

def rnd_select(count, large):
    result = []
    while len(result) < count:
        new_value = random.randint(1, large)
        if new_value not in result:
            result.append(new_value)
    return result

count = 6
large = 49
result = rnd_select(count, large)
print(result)

try:
    result = set(result)
    #changing result to a set to verify all numbers are unique
    assert len(result) == 6
    for number in result:
        assert number in range(1, large + 1)
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

