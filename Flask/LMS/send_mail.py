import smtplib
from email.mime.text import *
from email.mime.multipart import *

def send_mail(reciver_email,subject,body):
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="ysdevn@gmail.com"
    sender_password="ntsh gjst forn ckyv"
    reciver_email=reciver_email
    msg=MIMEMultipart()
    msg['From']=sender_email
    msg['To']="Undisclosed Recipients"
    msg['Subject']=subject
    msg.attach(MIMEText(body,'plain'))

    with smtplib.SMTP(smtp_server,port) as server:
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,reciver_email,msg.as_string())
        print("Mail send")


