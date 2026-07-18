'''a=3
def check1():
    print("inside val is",a)
check1()
print("the outside val is ",a)'''

'''a=3
def check2():
    a=5
    a=a**2
    print("val is",a)
check2()
print("the val ofa is",a)'''

'''a=3
def check3():
    a=7
    print("inside valis",a)
    a=10
    print("update val is",a+5)
    b=14
    b=b+a
    print("new val is",b)
check3()
print("the val of a ",a)'''

'''a=3
def check3():
    global a
    print("inside valis",a)
    a=10
    print("update val is",a+5)
    global b
    b=14
    b=b+a
    print("new val is",b)
check3()
print("the val of a ",a)
print("the val of b",b)'''



students=int(input("no ofstudents"))
p=0
a=0
for i in range(1,students+1):
    
    att=input("enter p or a:")
    if att=="p":
        print("present")
        p+=1
    else:
        a+=1
print("total students is : ",students)
print("total present is : ",p)
print("total absent is : ",a)
    
        




    
