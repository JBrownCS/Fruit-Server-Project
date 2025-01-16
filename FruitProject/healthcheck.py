'''
This checks the health of the computer every 60 seconds and sends an email if:

1) CPU usage is over 80%
2) Available disk space is lower than 20%
3) Available memory is less than 100MB
4) hostname "localhost" cannot be resolved to "127.0.0.1"
'''

import emails
import os
import psutil
import socket
import shutil


#Setup email sender, recipient, body
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

#Check if Disk usage is above 20%
dUsage = shutil.disk_usage("/")
percent_free = 100 * dUsage.free / dUsage.total
if percent_free < 20:
   subject = "Error - Available disk space is less than 20%"
   message = emails.create_message(sender, receiver, subject, body, attachment_path=None)
   emails.send(message)

#Check if CPU Usage is over 80%
cUsage = psutil.cpu_percent(1)
if cUsage < 80:
   subject = "Error - CPU usage is over 80%"
   message = emails.create_message(sender, receiver, subject, body, attachment_path=None)
   emails.send(message)

# Checks for available memory, if < 100mb sends an email
mem_size = psutil.virtual_memory()
if mem_size < (100 * 1024 * 1024):
   subject = "Error - Available memory is less than 100MB"
   message = emails.create_message(sender, receiver, subject, body, attachment_path=None)
   emails.send(message)

#Checks if localhost cannot be resolved to 127.0.0.1
hostname = socket.gethostbyname('localhost')
if hostname != '127.0.0.1':
   subject = "Error - Available memory is less than 100MB"
   message = emails.create_message(sender, receiver, subject, body, attachment_path=None)
   emails.send(message)




