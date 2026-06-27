Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
b=5.6
type(b)
<class 'float'>
c="jyeshi"
type(c)
<class 'str'>
d=3+5j
type(d)
<class 'complex'>
e=3i+4
SyntaxError: invalid decimal literal
f=3j+4
type(f)
<class 'complex'>
g=true
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    g=true
NameError: name 'true' is not defined. Did you mean: 'True'?
g="true"
type(g)
<class 'str'>
h= false
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    h= false
NameError: name 'false' is not defined. Did you mean: 'False'?
h="false"
type(h)
<class 'str'>
