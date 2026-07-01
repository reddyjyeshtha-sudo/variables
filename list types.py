Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#CONCATENATION
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname=jyeshtha
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fname=jyeshtha
NameError: name 'jyeshtha' is not defined
fname="jyeshtha"
lname="reddy"
print(fname +" "+lname)
jyeshtha reddy
print((fname+ " " +lname).title())
Jyeshtha Reddy




#FORMATING
a=2
b=6
print("the sum is",a+b)
the sum is 8
city="vja"
print("the city is",city)
the city is vja



a="mothu"
b="patlu"
print("hello {}{}".format(a,b))
hello mothupatlu
print("hello {}  {}".format(a,b))
hello mothu  patlu
print("hello {} hello {}".format(a,b))
hello mothu hello patlu


#FSTRING
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
print(f"hello {a} hello {b}")
hello sita hello ram


#multiplication(task)
a=6
b=7
print("the multiplication of {}{}".format(a,b,a*b))
the multiplication of 67
print("the multiplication of {}{} is {}".format(a,b,a*b))
the multiplication of 67 is 42

#MULTIPLICATION USING FSTRING
print(f"the product is {a}{b}")
the product is 67
print(f"the product is {a}{b} is {a * b}")
the product is 67 is 42


#list
a=[3,5.4,"python",5+8j,True]
print(a)
[3, 5.4, 'python', (5+8j), True]
typr(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    typr(a)
NameError: name 'typr' is not defined. Did you mean: 'type'?
type(a)
<class 'list'>

#LIST(1) APPEND
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']

#EXTEND(2)
b=["python","java","c++"]
b.extend()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    b.extend()
TypeError: list.extend() takes exactly one argument (0 given)
b.extend["js","bs"]
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    b.extend["js","bs"]
TypeError: 'builtin_function_or_method' object is not subscriptable
b.extend(["js","bs"])
b
['python', 'java', 'c++', 'js', 'bs']

#INSERT

b=["apple","banana","mango"]
b.insert(1,"grapes")
b
['apple', 'grapes', 'banana', 'mango']


#SORT
b=[7,6,3,4,9,0,1]
b.sort()
b
[0, 1, 3, 4, 6, 7, 9]
b=[7,6,3,4,9,0,1,1]
b.sort()
b
[0, 1, 1, 3, 4, 6, 7, 9]

#REVERSE
a=["java","python","c++"]
a.reverse()
a
['c++', 'python', 'java']

#pop
c=["python","java","c++","c"]
c.pop(2)
'c++'
c
['python', 'java', 'c']


#REMOVE
a=["black","white","red","pink"]
a.remove("white")
a
['black', 'red', 'pink']

#COPY
a=["jyesh","praneetha","teja"]
a.copy()
['jyesh', 'praneetha', 'teja']
b=a.copy()
b
['jyesh', 'praneetha', 'teja']
a.clear[]
SyntaxError: invalid syntax
a.clear()
a
[]
b.append("hi")
b
['jyesh', 'praneetha', 'teja', 'hi']
a
[]
