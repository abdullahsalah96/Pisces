import csv
from DatabaseClass import Database

database = Database()

data = database.printUsers()
f = open('outfile','w+')
writer = csv.writer(f)
for row in data:
    writer.writerow(row)

print(data)


###################Send grid#########################
import sendgrid
import os
from sendgrid.helpers.mail import *
import base64

sg = sendgrid.SendGridAPIClient(apikey = "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")
from_email = Email("test@example.com")
to_email = Email("abdullahsalah96@outlook.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
with open('/home/abdullahsalah96/International Codes/Microsoft-Azure-Challenge-2019/outfile.csv', 'rb') as fd:
     b64data = base64.b64encode(fd.read())
attachment = Attachment()
attachment.content = str(b64data,'utf-8')
attachment.filename = "your-lead-report.csv"

mail = Mail(from_email, subject, to_email, content)
mail.add_attachment(attachment)

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
############################################################
