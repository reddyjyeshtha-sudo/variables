Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="jyeshtha"
a[0]
'j'
a[4]
'h'
b = "simple is better than complex"
b[10]
'b'
b[10]+b[11]+b[12]+b[13]+b[14]+b[15]
'better'
b[22]+b[23]+b[24]+b[25]+b[26]+b[27]
'comple'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]
'simple'
c="codegnan it solutions"
c[12]+c[13]+c[14]+c[15]+c[16]+c[17]
'soluti'
#NEGTIVE INDEXING
d="jyeshtha is good girl"
d[-9]+d[-8]+d[-7]+d[-6]
'good'
d[-20]+d[-19]+d[-18]+d[-17]+d[-16]+d[-15]+d[-14]+d[-13]
'yeshtha '
d[-21]+d[-20]+d[-19]+d[-18]+d[-17]+d[-16]+d[-15]+d[-14]+d[-13]
'jyeshtha '




#slicing
r="time is very precious"
r[10:14]
'ry p'
r[8:12]
'very'
r[13:21]
'precious'
r[:4]
'time'
j="vizag is city of destiny"
j[-14:-10]
'ity '
j[-15:-10]
'city '
j[-1:-8]
''
j[-1:-7]
''
j[-19:-24]
''
j[-7:-1]
'destin'
j[-24:19]
'vizag is city of de'
j[-24:-19]
'vizag'
j[-7:-1]
'destin'
j[-7:]
'destiny'
i="data science"
[ : :3]
SyntaxError: invalid syntax
k="machine learning"
q="cloud computing"
q[1:9:2]
'lu o'
i="data science"
i[0:9:2]
'dt ce'
