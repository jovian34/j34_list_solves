'''
https://sites.google.com/site/prologsite/prolog-problems/1
1.19 (**) Rotate a list N places to the left.
Examples:
?- rotate([a,b,c,d,e,f,g,h],3,X).
X = [d,e,f,g,h,a,b,c]

?- rotate([a,b,c,d,e,f,g,h],-2,X).
X = [g,h,a,b,c,d,e,f]

Hint: Use the predefined predicates length/2 and append/3, as well as the result of problem 1.17.

A list is either empty or it is composed of a first element (head)
and a tail, which is a list itself. In Prolog we represent the
empty list by the atom [] and a non-empty list by a term [H|T]
where H denotes the head and T denotes the tail.
'''

my_list = ['a','b','c','d','e','f','g','h']

def rotate_list(n):
    if n < 0:
        index = len(my_list) + n
    else:
        index = n
    new_list = my_list[ index : ]
    for i in range(index):
        new_list.append(my_list[i])
    return new_list
    
result_1 = rotate_list(3)
result_2 = rotate_list(-2)

print(result_1)
print(result_2)

try:
    assert result_1 == ['d','e','f','g','h','a', 'b', 'c']
    assert result_2 == ['g','h','a', 'b', 'c', 'd','e','f']
    print('You got the result you wanted. You are a ROCK STAR!')
except AssertionError:
    print('This has failed miserably. Do it again!')

