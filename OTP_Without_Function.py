#Task-1: Implement a program in Java/Python to generate One Time Password and send it to the
#registered email ID or mobile number.

#1.Generate OTP ---- By using Random Module
#2.Send OTP to Users email address ---- Smptlib Module
#smptlib stands for Simple Mail Transfer Protocol client

# Four Digit OTP ---- 3251,4058,3880

import random
import smtplib

#otp = ''.join([str(random.randint(0,9)) for i in range(4)])
#print(otp)

server = smtplib.SMTP('smtp.gmail.com',587)

#print(server)

server.starttls()

server.login('hemangi.gavande29@gmail.com',password)

otp = ''.join([str(random.randint(0,9)) for i in range(4)])


msg="Hello, Your OTP is "+str(otp)

server.sendmail('hemangi.gavande29@gmail.com','ruddhibhagat2402@gmail.com',msg)

server.quit()




