Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=2
b=6
print(a+b)
8
print(a-b)
-4
print(a*b)
12
print(a/b)
0.3333333333333333
print(a//b)
0
print(a**b)
64
a=2
b=6
print(a+=b)
SyntaxError: invalid syntax
a+b
8
a+=b
a
8
a
8
a=-2
a
-2
b
6
b=-2
b
-2
a**=4
a
16
a/=2
a
8.0
a*=3
a
24.0
a%=6
a
0.0
b+=6
b
4
b-=6
b
-2
b*=6
b
-12
b/=6
b
-2.0
a=4
b=8
a<b
True
b>a
True
a>b
False
a==b
False
a!=b
True
a=2
b=6
a<b and b>a
True
a!=b and b!=a
True
a!=b or b==a
True
#identify operators
a=26
type(a) is int
True
type(a) is not int
False
b=2.4
type(a) is float
False
c="jyeshi"
type(c) is string
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    type(c) is string
NameError: name 'string' is not defined
c="jyeshi"
type("c") is string
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    type("c") is string
NameError: name 'string' is not defined
d="true"
type(d) is boolean
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    type(d) is boolean
NameError: name 'boolean' is not defined
c=jyeshi
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    c=jyeshi
NameError: name 'jyeshi' is not defined
c="jyeshi"
type(c) is str
True
type(c) is not str
False
d=true
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    d=true
NameError: name 'true' is not defined. Did you mean: 'True'?
d = True
type(d) is bool
True
type(d) is not bool
False
a=3,4,5,6,7,8,9,10
4 in a
True
20 in a
False
20 not in a
True
a=2
b=6
a & b
2
bin(2)
'0b10'
bin(4)
'0b100'
bin(6)
'0b110'
bin(8)
'0b1000'
a=2
b=6
a|b
6
a=2
-(a+1)
-3
-a
-2
a=5
-a
-5
a=9
-a
-9
a=6
b=9
a^b
15
a=5
b=7
a^b
2
