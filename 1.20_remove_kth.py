'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.20 (*) Remove the K'th element from a list.
Example:
?- remove_at(X,[a,b,c,d],2,R).
X = b
R = [a,c,d]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''


def remove_at(x_letter, list_of_letters):
    result_list = []
    for letter in list_of_letters:
        if letter != x_letter:
            result_list.append(letter)
    return result_list

my_list = ['a','b','c','d']
x = 'b'
result = remove_at(x, my_list)
print(result)

try:
    assert result == ['a','c','d']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

