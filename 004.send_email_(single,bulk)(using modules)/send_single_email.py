#import modules

import smtplib              #for simple transfer protocal
from email.mime.text import MIMEText                        #mime text is used to add the text 
from email.mime.multipart import MIMEMultipart              #mimemultiepart is used  to combine the like single part subject, body,reciver mail


#configuration
sender_email="yeswithapirakala1234@gmail.com"
sender_password="akjmfuspqwhoiuhj"
smtp_server="smtp.gmail.com"
smtp_port=587

#creating single sender function
def singleemailsend(to_email:str, subject:str, body:str):
    #creating the email message
    msg=MIMEMultipart()
    msg['To']=to_email
    msg["From"]=sender_email
    msg["Subject"]=subject
    msg.attach(MIMEText(body,'plain'))

    try:
        #create server connection 
        server=smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()                                        #start connecting to server
        server.login(sender_email, sender_password)              #login to server
        server.sendmail(sender_email, to_email, msg.as_string()) #send email
        server.quit()                                            #quit from the server,server closed


        print(f"sucessfully send email to {to_email}")

    except Exception as e:
        print(f"failed to send the email to {to_email} and error:{e}")


