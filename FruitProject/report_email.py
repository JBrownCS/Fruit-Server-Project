#Read data from description txt files to generate a pdf
import datetime
import emails
import os
import sys
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


#Generate pdf based on a given filename, title, body text, and table data
def generate_report(filename, title, body_text):
    report = SimpleDocTemplate(filename)
    #get styles from style sheet
    styles = getSampleStyleSheet()
    #Create a title with h1 header style
    report_title = Paragraph(title, styles["h1"])
    #Use the text from the description txt files as the body
    report_info = Paragraph(body_text, styles["BodyText"])
    report.build([report_title, report_info])


#The body text will have each fruit's name and weight from the files
def create_body_text():
    
    #establish current directory for all descriptions that need to be posted to the server
    current_desc_dir = os.path.dirname(os.path.abspath(sys.argv[0])) + '/supplier-data/descriptions'

    #body text
    body = ""

    os.chdir(current_desc_dir)
    #Loop through directory and collect post data
    for file in os.listdir(current_desc_dir):

        #Read file
        desc_file = open(file, 'r')
        desc_info = desc_file.readlines()

        '''
        Line 1 is the Fruit Name
        Line 2 is the fruit weight
        '''
        body += "".join([
            desc_info[0] + "<br/>",desc_info[1] + "<br/>","<br/>"])
        
        desc_file.close()
    
    return body

#Get filepath for pdf generated, title with today's date and body for report function
filepath = os.path.dirname(os.path.abspath(sys.argv[0])) + '/tmp/processed.pdf'
date_str = datetime.datetime.today().strftime('%B %d, %Y')
title = "Processed Update on " + date_str
body_text = create_body_text()
generate_report(filename=filepath, title=title, body_text=body_text)
    
#Generate email of report as well once it is generated
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Fruits Report"
body = "Here is the fruit report pdf of all fruits with their weights."
attachment_path = filepath

message = emails.create_message(sender, receiver, subject, body,attachment_path=attachment_path)
emails.send(message)
