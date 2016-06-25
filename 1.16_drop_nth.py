'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.16 (**) Drop every N'th element from a list.
Example:
?- drop([a,b,c,d,e,f,g,h,i,k],3,X).
X = [a,b,d,e,g,h,k]

Carl James' solution in Python 3.5.1 is below
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

