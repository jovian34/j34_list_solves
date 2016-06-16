'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.10 (*) Run-length encoding of a list.
Use the result of problem 1.09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as terms [N,E] where N is the number of duplicates of the element E.

Example:
?- encode([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],[1,b],[2,c],[2,a],[1,d][4,e]]

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
    result.append([len(list),list[0]])

print(result)

try:
    assert result == [[4,'a'],[1,'b'],[2, 'c'],[2,'a'],[1, 'd'],[4,'e']]
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

