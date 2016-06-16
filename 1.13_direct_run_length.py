'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.13 (**) Run-length encoding of a list (direct solution).
Implement the so-called run-length encoding data compression
method directly. I.e. don't explicitly create the sublists
containing the duplicates, as in problem 1.09, but only count
them. As in problem 1.11, simplify the result list by replacing
the singleton terms [1,X] by X.

Example:
?- encode_direct([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],b,[2,c],[2,a],d,[4,e]]

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
result = []
current_letter = my_list[0]
current_count = 1
for i in range(1,len(my_list)):
    if my_list[i] == current_letter:
        current_count += 1
    elif current_count == 1:
        result.append(my_list[i-1])
        current_letter = my_list[i]
    else:
        result.append([current_count, my_list[i-1]])
        current_letter = my_list[i]
        current_count = 1
if current_count == 1:
    result.append(my_list[-1])
else:
    result.append([current_count, my_list[-1]])

print(result)

try:
    assert result == [[4,'a'],'b',[2, 'c'],[2,'a'],'d',[4,'e']]
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

