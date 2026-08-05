#Email automation
import random
import math
import smtplib#simple mail transfer protocol library-used to send otp

digits="0123456789" #should be in string.int,float is not acceptable.
OTP=""#empty string

for i in range(6): #otp in 6 digits
    OTP+=digits[math.floor(random.random()*10)] #otp is caluculated
otp=OTP+"is your otp" # 678646 stored in variable otp
msg=otp

s=smtplib.SMTP("smtp.gmail.com",587) 
s.starttls()
s.login("jyeshthareddy26@gmail.com","gtcd zofk untw vsep")
user="jyeshthareddy26@gmail.com"

emailid=input("enter the email which you want to send otp")
s.sendmail(user,emailid,msg)

while True:
    a=input("enter the otp")
    if a==OTP:
        print("otp is correct")
    else:
        print("incorrect otp")
