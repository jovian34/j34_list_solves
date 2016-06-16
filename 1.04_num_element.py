Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.03_kth_element.py ====
10
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.05_reverse.py ======
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.05_reverse.py ======
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
You got the result you wanted. You are a ROCK STAR!
>>> 
===== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py =====
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 28, in <module>
    result = even_palindrome(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 13, in even_palindrome
    for i in range( (len(my_list))/ 2 ):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
===== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py =====
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 30, in <module>
    result = even_palindrome(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 14, in even_palindrome
    for i in range(length_list):
NameError: name 'length_list' is not defined
>>> 
===== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py =====
True
You got the result you wanted. You are a ROCK STAR!
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 48, in <module>
    result = odd_palindrome(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py", line 21, in odd_palindrome
    for i in range(length_list):
TypeError: 'float' object cannot be interpreted as an integer
>>> 
===== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.06_palindrome.py =====
True
You got the result you wanted. You are a ROCK STAR!
True
You got the result you wanted. You are a ROCK STAR!
False
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
[]
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 30, in <module>
    flatten_list(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 24, in flatten_list
    for i in range(length(list)):
NameError: name 'length' is not defined
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 30, in <module>
    flatten_list(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 26, in flatten_list
    result.append[list[i]]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', 'b', 'c', 'd']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 30, in <module>
    flatten_list(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 28, in flatten_list
    return flatten_list(list[i])
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 28, in flatten_list
    return flatten_list(list[i])
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 25, in flatten_list
    if len(list[i]) == 1:
IndexError: list index out of range
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', 'b', 'c', 'd']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e']]
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
not a list a
not a list ['b', ['c', 'd'], 'e']
['a', ['b', ['c', 'd'], 'e']]
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
<class 'str'>
not a list a
<class 'list'>
not a list ['b', ['c', 'd'], 'e']
['a', ['b', ['c', 'd'], 'e']]
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 30, in <module>
    flatten_list(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 25, in flatten_list
    if isinstance(list[i], list):
TypeError: isinstance() arg 2 must be a type or tuple of types
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 32, in <module>
    flatten_list(my_list)
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 25, in flatten_list
    if isinstance(list[i], basestring):
NameError: name 'basestring' is not defined
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', 'b', 'c', 'd']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e']]
['b', ['c', 'd'], 'e']
['c', 'd']
['a', 'b', 'c', 'd']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e']]
['b', ['c', 'd'], 'e']
['c', 'd']
['a', 'b', 'c', 'd', 'e']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e'], ['f', 'g', ['h', 'i', 'j'], 'k'], 'l']
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', ['h', 'i', 'j'], 'k']
['h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e'], ['f', 'g', ['h', 'i', 'j'], 'k'], 'l']
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', ['h', 'i', 'j'], 'k']
['h', 'i', 'j']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', ['b', ['c', 'd'], 'e'], ['f', 'g', ['h', 'i', 'j'], 'k'], ['l', 'm'], 'n']
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', ['h', 'i', 'j'], 'k']
['h', 'i', 'j']
['l', 'm']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', [['b', ['c', 'd'], 'e'], ['f', 'g', ['h', 'i', 'j'], 'k'], ['l', 'm'], 'n']]
[['b', ['c', 'd'], 'e'], ['f', 'g', ['h', 'i', 'j'], 'k'], ['l', 'm'], 'n']
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', ['h', 'i', 'j'], 'k']
['h', 'i', 'j']
['l', 'm']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', [[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']], ['l', 'm'], 'n']]
[[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']], ['l', 'm'], 'n']
[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']]
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', [[['h'], 'i'], 'j'], 'k']
[[['h'], 'i'], 'j']
[['h'], 'i']
['h']
['l', 'm']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['a', [[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']], ['l', 'm'], 'n']]
[[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']], ['l', 'm'], 'n']
[['b', ['c', 'd'], 'e'], ['f', 'g', [[['h'], 'i'], 'j'], 'k']]
['b', ['c', 'd'], 'e']
['c', 'd']
['f', 'g', [[['h'], 'i'], 'j'], 'k']
[[['h'], 'i'], 'j']
[['h'], 'i']
['h']
['l', 'm']
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['alpha', [[['bravo', ['charlie', '4'], '5.32'], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ['love', 'madre'], 'november']]
[[['bravo', ['charlie', '4'], '5.32'], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ['love', 'madre'], 'november']
[['bravo', ['charlie', '4'], '5.32'], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']]
['bravo', ['charlie', '4'], '5.32']
['charlie', '4']
['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']
[[['hotel'], 'indigo'], 'juliet']
[['hotel'], 'indigo']
['hotel']
['love', 'madre']
['alpha', 'bravo', 'charlie', '4', '5.32', 'foxtrot', '7', 'hotel', 'indigo', 'juliet', 'kilo', 'love', 'madre', 'november']
This has failed miserably. Do it again!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['alpha', [[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']]
[[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']
[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']]
['bravo', ['c', 4], 5.32]
['c', 4]
['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']
[[['hotel'], 'indigo'], 'juliet']
[['hotel'], 'indigo']
['hotel']
('love', 'madre')
['alpha', 'bravo', 'c', 4, 5.32, 'foxtrot', '7', 'hotel', 'indigo', 'juliet', 'kilo', 'love', 'madre', 'november']
You got the result you wanted. You are a ROCK STAR!
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
Traceback (most recent call last):
  File "/Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py", line 19, in <module>
    my_list = ['alpha', [[['bravo', ['c', 4], 5.32], [FALSE, '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']]
NameError: name 'FALSE' is not defined
>>> 
====== RESTART: /Users/carljame/Box Sync/Coding/prolog/1.07_flatten.py ======
['alpha', [[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']]
[[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']], ('love', 'madre'), 'november']
[['bravo', ['c', 4], 5.32], ['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']]
['bravo', ['c', 4], 5.32]
['c', 4]
['foxtrot', '7', [[['hotel'], 'indigo'], 'juliet'], 'kilo']
[[['hotel'], 'indigo'], 'juliet']
[['hotel'], 'indigo']
['hotel']
('love', 'madre')
['alpha', 'bravo', 'c', 4, 5.32, 'foxtrot', '7', 'hotel', 'indigo', 'juliet', 'kilo', 'love', 'madre', 'november']
You got the result you wanted. You are a ROCK STAR!
>>> 
