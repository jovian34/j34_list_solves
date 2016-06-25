'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.07 (**) Flatten a nested list structure.
Transform a list, possibly holding lists as elements into a 'flat' list by replacing each list with its elements (recursively).

Example:
?- my_flatten([a, [b, [c, d], e]], X).
X = [a, b, c, d, e]

Hint: Use the predefined predicates is_list/1 and append/3

Carl James' solution in Python 3.5.1 is below
'''


my_list = ['alpha', [[['bravo', ['c', 4], 5.32], [ 'foxtrot' , '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']]
result = []

def flatten_list(list):
    print(list)
    for i in range(len(list)):
        if isinstance(list[i], (str, int, float, bool)):
            result.append(list[i])
        else:
            flatten_list(list[i])

flatten_list(my_list)
print(result)

try:
    assert result == ['alpha', 'bravo', 'c', 4, 5.32, 'foxtrot' , '7', 'hotel', 'indigo', 'juliet', 'kilo', 'love', 'madre', 'november']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

