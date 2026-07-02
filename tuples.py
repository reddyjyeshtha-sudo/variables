Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=(4,5.4,"jyeshtha",8+7j,True,False)
print(a)
(4, 5.4, 'jyeshtha', (8+7j), True, False)
type(a)
<class 'tuple'>
len(a)
6
a.index(8+7j)
3
a.count(True)
1


#SETS
a={3,4.5,True,False,8+9j}
print(a)
{False, True, 3, 4.5, (8+9j)}
type(a)
<class 'set'>
#SUBSET
a={2,4,5,6,7,8,9}
b={7,8,9}
b.issubset(a)
True
a.issubset(b)
False

#superset
a={6,7,8,9,3,4}
b={7,8,9}
a.issuperset(b)
True

#union
a={6,7,8,9,3,4}
b={1,2,3,4,5}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}


#INTERSECTION
a={6,7,8,9,3,4}
b={8,9,1,3}
a.intersection(b)
{8, 9, 3}


#DIFFERENCE
a={10,11,12,13,14,15,16}
b={6,7,8,11,12,13,14,15,16,2}
a.difference(b)
{10}
b.difference(a)
{8, 2, 6, 7}

#SYMMETRIC DIFF
a={5,6,7,8,9}
b={7,8,9,1,2}
a.symmetric_difference(b)
{1, 2, 5, 6}
b.symmetric_difference(a)
{1, 2, 5, 6}


#UPDATE
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update
<built-in method update of set object at 0x0000017D32C652A0>
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}

#POP AND REMOVE
a={5,6,7,8,9}
a.pop()
5
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.remove(5)
KeyError: 5
a=[9,1,5,2,8,4,6,3,7,0]
b=a[:5]
b
[9, 1, 5, 2, 8]
c=a[5:]
c
[4, 6, 3, 7, 0]
