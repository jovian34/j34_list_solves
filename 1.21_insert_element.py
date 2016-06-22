'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.21 (*) Insert an element at a given position into a list.
Example:
?- insert_at(alfa,[a,b,c,d],2,L).
L = [a,alfa,b,c,d]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.

Prolog problem is above

Carl James' solution on Python 3.5.1 is below
'''


def insert_at(index, x_letter, list_of_letters):
    result_list = []
    i = 1
    for letter in list_of_letters:
        if i == index:
            result_list.append(x_letter)            
        result_list.append(letter)
        i += 1
    return result_list

my_list = ['a','b','c','d']
x = 'alfa'
index = 2
result = insert_at(index, x, my_list)
print(result)

try:
    assert result == ['a','alfa','b','c','d']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

