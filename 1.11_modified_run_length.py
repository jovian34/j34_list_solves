'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.11 (*) Modified run-length encoding.
Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.

Example:
?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
X = [[4,a],b,[2,c],[2,a],d,[4,e]]

Carl James' solution in Python 3.5.1 is below
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
        result.append([len(list),list[0]])

print(result)

try:
    assert result == [[4,'a'],'b',[2, 'c'],[2,'a'],'d',[4,'e']]
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

