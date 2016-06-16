'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.16 (**) Drop every N'th element from a list.
Example:
?- drop([a,b,c,d,e,f,g,h,i,k],3,X).
X = [a,b,d,e,g,h,k]



A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c','d','e','f','g','h','i','k']
result = []

for i in range(0, len(my_list)):
    if (i+1) % 3 == 0:
        pass
    else:
        result.append(my_list[i])
print(result)

try:
    assert result == ['a', 'b', 'd', 'e', 'g', 'h', 'k']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

