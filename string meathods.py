Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="python course"
a[-1:-11:-3]
'eu h'
a[-2:-12:-4]
'sch'
a[-5:-13:-5]
'oh'
#REVERSE STRING
a[::-1]
'esruoc nohtyp'


#STRING MEATHODS
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#COUNT
e="jyeshtha jyeshtha"
e.count(h)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    e.count(h)
NameError: name 'h' is not defined
e.count("h")
4
f="jyeshthajyeshtha"
f.count("h")
4
#FIND THE STRING
g="jyeshtha"
g.find['s']
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    g.find['s']
TypeError: 'builtin_function_or_method' object is not subscriptable
g.find["s"]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    g.find["s"]
TypeError: 'builtin_function_or_method' object is not subscriptable
g.find("s")
3
g.find("m")
-1
#ESCAPE SEQUENCES
h="name:jyeshtha\nmobileno: 123456789\nmailid:reddy@gmail.com\ncollege:griet\tbranch:csbs
SyntaxError: unterminated string literal (detected at line 1)
h="name:jyeshtha\nmobileno: 123456789\nmailid:reddy@gmail.com\ncollege:griet\tbranch:csbs"
print(h)
name:jyeshtha
mobileno: 123456789
mailid:reddy@gmail.com
college:griet	branch:csbs
#REPLACE
i="wait until you succeseed
SyntaxError: unterminated string literal (detected at line 1)
i="wait until you succeseed"
i.replace("wait","work")
'work until you succeseed'
j="i love python"
j.replace("python","java")
'i love java'
#uppercase lowercase tittle
k="hello"
k.upper()
'HELLO'
l="python"
l.lower()
'python'
m="python course"
m.title()
'Python Course'
m.capitalize()
'Python course'
#is
n="python"
n.isupper()
False
o="python course"
o.isalpha()
False
p="pythoncourse"
a.isalpha()
False
p.isalpha()
True
r="1234"
r.isdigit()
True
s="jyesh1234()
SyntaxError: unterminated string literal (detected at line 1)
s="jyeshi12345"
s.isalnum()
True
#startswith endswith
a="java"
a.startswith("a")
False
a.endswith("a)
           
SyntaxError: unterminated string literal (detected at line 1)
a.endswith("a")
           
True
#strips
           
"       pooja     "
           
'       pooja     '
j="       pooja    "
           
j.strip()
           
'pooja'
j.lstrip()
           
'pooja    '
j.rstrip()
           
'       pooja'
#SPLIT
           
a="python java c c++"
           
a.split()
           
['python', 'java', 'c', 'c++']
#JOIN
           
b="" vja hyd vizag"
           
SyntaxError: unterminated string literal (detected at line 1)
b="vja hyd vizag"
           
"".join(b)
           
'vja hyd vizag'
" ".join(b)
           
'v j a   h y d   v i z a g'
