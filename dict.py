Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[9,1,5,2,8,4,6,3,7,0,]
b=a[:5]
b
[9, 1, 5, 2, 8]
c=a[5:10]
c
[4, 6, 3, 7, 0]
b.sort()
b
[1, 2, 5, 8, 9]
c.sort()
c
[0, 3, 4, 6, 7]
b.reverse()
b
[9, 8, 5, 2, 1]
c.reverse()
c
[7, 6, 4, 3, 0]
d=c+b
d
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]

#DICT
a={"name":jyeshtha,"year":2026,"month":6}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a={"name":jyeshtha,"year":2026,"month":6}
NameError: name 'jyeshtha' is not defined
a={"name":"jyeshtha","year":2026,"month":6}
print(a)
{'name': 'jyeshtha', 'year': 2026, 'month': 6}
type(a)
<class 'dict'>

#updaate
a={"name":"jyeshtha","year":2026,"month":6}
a.update({"month":12,"year":2026})
a
{'name': 'jyeshtha', 'year': 2026, 'month': 12}
a={"name":"jyeshtha","year":2026,"month":6}
a.update({"age":12,"year":2026})
a
{'name': 'jyeshtha', 'year': 2026, 'month': 6, 'age': 12}


#SETDEFAULT
a={"course":"python"}
a.setdefault("duration",4)
4
a
{'course': 'python', 'duration': 4}


#accesing
a={"food":"biryani","colour":"black"}
a=["colour"]
a
['colour']

a.get("food")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.get("food")
AttributeError: 'list' object has no attribute 'get'
a.get("biryani")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a.get("biryani")
AttributeError: 'list' object has no attribute 'get'
a={"food":"biryani","colour":"black"}
a["colour"]
'black'

a.get("food")
'biryani'

#keys and values
a={"name":"jyeshtha","year":2026,"month":6}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['jyeshtha', 2026, 6])
a.items()
dict_items([('name', 'jyeshtha'), ('year', 2026), ('month', 6)])

#pop
a={"country":"india","state":"ap","city":"vja"}
a.pop("city")
'vja'
a
{'country': 'india', 'state': 'ap'}
a.popitem()
('state', 'ap')
a
{'country': 'india'}

#len copy clear
a={"name":"jyeshtha","year":2026,"month":6}
len(a)
3
a.copy()
{'name': 'jyeshtha', 'year': 2026, 'month': 6}
a.clear()
a
{}

a={"idnos":["2,4,6"],"names":["jyesh","sweeety","hearty"]}
a.keys()
dict_keys(['idnos', 'names'])
a.values()
dict_values([['2,4,6'], ['jyesh', 'sweeety', 'hearty']])
a.items()
dict_items([('idnos', ['2,4,6']), ('names', ['jyesh', 'sweeety', 'hearty'])])






a=["codegnan","python"]
a.upper()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
uppercase_a=[a.upper() for a in wordsAttributeError: 'list' object has no attribute 'upper'
             
SyntaxError: invalid syntax


a=["codegnan","python"]
             
b=str(a)
             
b.upper()
             
"['CODEGNAN', 'PYTHON']"
