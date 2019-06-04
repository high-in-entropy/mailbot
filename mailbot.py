# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:37:31 2019

@author: Viraj Mohile (high_in_entropy)
"""

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

##### Read sender and receiver emails using pandas #####

r_emails = pd.read_excel("./emails/final_emails.xlsx")
s_emails = pd.read_excel("./emails/sender_emails.xlsx")

##### Section over #####

##### Calculate the number of emails required to send. Considering 150 as the Gmail limit #####

no = len(r_emails)
req = no / 150

if(no % 150 != 0):
    req = int(req) + 1
else:
    req = int(req)
    
if(len(s_emails) < req):
    import sys
    sys.exit("Error! You don't have enough email ids to send that much of emails!")
    
##### Section OVER #####

r_emails['Mail'] = r_emails['Mail'].str.lower() ##IN CASE YOU HAVE ERRONEOUS UPPERCASE EMAIL IDS ##



for i in range(req):
    
    if(i != req - 1):
        end = 150*(i+1)
    else:
        end = no
        
    receivers = r_emails['Mail'].iloc[range(150*i, end),]
    receivers = pd.DataFrame(receivers)
    receivers = receivers.reset_index()
    
    for j in range(end - (150*i)):
        sender_email = s_emails['Mail'][i]
        receiver_email = receivers['Mail'][j]
        password = s_emails['Password'][i]
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Freeco online Education!"
        message["From"] = sender_email
        message["To"] = receiver_email
        
        ##### CREATING PLAIN TEXT AND HTML MESSAGE THAT NEEDS TO BE SENT #####  
        
        with open('./message/text.txt', 'r') as file:
            data = file.read()
        data = data.replace("\n", "")
        
        text = data
        
        with open('./message/html.txt', 'r') as file:
            data = file.read()
        data = data.replace("\n", "")
        
        html = data
        
        
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(
                        sender_email, receiver_email, message.as_string()
                        )
                print("Mail Sent Successfully", " NO : ", str((150*i)+j))
        except:
            print("Email adderess Invalid", " NO: ", str((150*i)+j))
                
        
