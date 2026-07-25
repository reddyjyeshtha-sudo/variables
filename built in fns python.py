'''print(dir("__builtins"))'''
'''a="code"
b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"jyeshi" )
print(b)

b["i"]="sam"
print(b)'''


#eval
'''a=eval(input("a val"))
b=eval(input("b val"))
print(a+b)'''

#zip
'''a=[10,20,30,40]
names=["jyesh","teja","praneetha","narsareddy"]
print(a+names)

b=list(zip(a,names))
print(b)'''

#enumerate
'''names={"jyeshi","praneetha"}
for i in range(len(names)):
    print(i,names)'''


'''names={"jyeshi","praneetha"}
b=dict(enumerate(names))
print(b)'''

#ascii
'''print(chr(65))
print(chr(90))
print(chr(5))

print(ord("a"))
print(ord("z"))'''

'''a=input("name")
for i in a:
    print(i,ord(i))'''

#max,min,sum
print(max(20,10,30,45))

print(min(20,10,30,45))

a=2,3,4,5,6,7
print(sum(a))



