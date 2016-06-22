'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.22 (*) Create a list containing all integers within a given range.
Example:
?- range(4,9,L).
L = [4,5,6,7,8,9]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.

Prolog problem is above

Carl James' solution on Python 3.5.1 is below
'''

def list_integers(start, end):
    result_list = []
    i = start
    while i <= end:
        result_list.append(i)
        i += 1
    return result_list

start = 4
end = 9
result = list_integers(start, end)
print(result)

try:
    assert result == [4,5,6,7,8,9]
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

