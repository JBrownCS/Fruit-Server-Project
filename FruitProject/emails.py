from email.message import EmailMessage
import os.path
import mimetypes
import smtplib



#Create the email message with from/to, subject, body 
# and pdf attachment path if needed (health check.py does not have one, but reports.py does)
def create_message(sender, recipient, subject, body, attachment_path=None):
    
    #Create email and enter basic sender/recipient/body data
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path != None:
        #Add PDF attachment based on the given filepath
        mime_type, _ = mimetypes.guess_type(attachment_path)

        mime_type, mime_subtype = mime_type.split("/",1)

        with open(attachment_path, 'rb') as pdf:
            message.add_attachment(pdf.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=os.path.basename(attachment_path))
        
    return message

#Send message through configured SMTP server
def send(message):
  
  mail_server = smtplib.SMTP('http://127.0.0.1:5500/')
  mail_server.send_message(message)
  mail_server.quit()
