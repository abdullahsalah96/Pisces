import sendgrid
import os
from sendgrid.helpers.mail import *
import base64

class emailNotifier():
    def __init__(self, sender, recipient):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.sender = Email(sender)
        self.recipient = Email(recipient)
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")

    def sendEmail(self, subject, body, attachementPath, attachementName):
        """
        a function that takes the subject and the body as input and sends an email
        """
        self.subject = subject
        self.body = Content("text/plain", body)
        # content = Content("text/plain", "and easy to do anywhere, even with Python")
        with open(attache+39/mentPath, 'rb') as fd:
             b64data = base64.b64encode(fd.read())
        attachment = Attachment()
        attachment.content = str(b64data,'utf-8')
        attachment.filename = attachementName
        self.message = Mail(self.sender, self.subject, self.recipient, self.body)
        self.message.add_attachment(attachment)
        response = self.sg.client.mail.send.post(request_body=self.message.get())
