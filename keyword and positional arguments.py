'''def details(id,name,mailid):
    id=10
    name="jyeshi"
    mailid="j@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="hari",mailid="why@gmail.com")'''

'''def grocery(item,price):
    print("item is %s"%item)
    print("item is %.2f"%price)
grocery("rice",200)'''

'''def grocery(item="rice",price=400):
    print("item is %s"%item)
    print("item is %.2f"%price)
grocery()'''

'''def bakery(cakename,price,quantity):
    print("cakename is %s" %cakename)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
bakery("chocolate",200,2000)'''


'''def bakery(cakename='chocolate',price=890,quantity=1000):
    print("cakename is %s" %cakename)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
bakery()'''

def bakery(cakename,price=500,quantity=1000):
    print("cakename is %s" %cakename)
    print("price is %d" %price)
    print("quantity is %d" %quantity)
bakery("chocolate")
            
    
