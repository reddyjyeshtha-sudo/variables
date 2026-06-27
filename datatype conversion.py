Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
int(8)
8
int(2.6)
2
int(3+7j)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int(3+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int("jyeshi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("jyeshi")
ValueError: invalid literal for int() with base 10: 'jyeshi'
int(true)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(false)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
float(8)
8.0
float(4.5)
4.5
float("jyeshi")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float("jyeshi")
ValueError: could not convert string to float: 'jyeshi'
float(4+7j)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float(4+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(true)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
float(false)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
string("7")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    string("7")
NameError: name 'string' is not defined
string(7)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    string(7)
NameError: name 'string' is not defined
string(4.7)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string(4.7)
NameError: name 'string' is not defined
string("jyeshi")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    string("jyeshi")
NameError: name 'string' is not defined
string(jyeshi)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    string(jyeshi)
NameError: name 'string' is not defined
string(7+9j)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    string(7+9j)
NameError: name 'string' is not defined
string(true)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    string(true)
NameError: name 'string' is not defined
string("true")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    string("true")
NameError: name 'string' is not defined
float(True)
1.0
float(False)
0.0
str(7)
'7'
str(7.8)
'7.8'
str(True)
'True'
str(False)
'False'
complex(8)
(8+0j)
complex(True)
(1+0j)
complex(False)
0j
bool(5)
True
bool(3.7)
True
bool("java")
True
bool(5.6j)
True
