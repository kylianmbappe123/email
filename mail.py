import os
os.system('cls')
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def emailsender(reciever,subject,content):
    hostmail='dotproduct456@gmail.com'
    hostpassword='wpaieaoevumeczav'
    recievermail=reciever
    
    asd=MIMEMultipart()
    asd['from']=hostmail
    asd['to']=recievermail
    asd['subject']=subject
    asd.attach(MIMEText(content,'plain'))

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(hostmail,hostpassword)
    text=asd.as_string()
    server.sendmail(hostmail,recievermail,text)
    server.quit()
    print("email is sent,\nyou are welcome for my service")


print("welcome to email sender")
con='no'
while con=='no':
    subject=input("type something spicy: ")
    content=input("enter email content:  ")
    reciever=input("enter reciever's email: ")


    print("comfirm details: ")
    print("reciever's mail: ",reciever)
    print("subject: ",subject)
    print("content: ",content)

    confirm=input("send?? (type yes/no):")
    if confirm=='yes':
        emailsender(reciever,subject,content)
        break
    else:
        con='no'



