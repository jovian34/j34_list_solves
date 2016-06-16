'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.12 (**) Decode a run-length encoded list.
Given a run-length code list generated as specified in
problem 1.11. Construct its uncompressed version.

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
result = [ [my_list[0]] ]
prior_letter = my_list[0]
for i in range(1, len(my_list)):
    if prior_letter != my_list[i]:
        result.append([my_list[i]])
    else:
        result[-1].append(my_list[i])
    prior_letter = my_list[i]
    
my_lists = result
result = []

for list in my_lists:
    if len(list) == 1:
        result.append(list[0])
    else:
        result.append([])
        for letter in list:
            result[-1].append(letter)

print(result)

try:
    assert result == [['a','a','a','a'],'b',['c', 'c'],['a','a'],'d',['e','e','e','e']]
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

