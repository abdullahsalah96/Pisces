import sendgrid
import os
from sendgrid.helpers.mail import *
import base64
from ExportToExcel import ExcelConverter
class emailNotifier():
    def __init__(self, sender, user):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.user = user
        self.sender = Email(sender)
        self.recipient = Email(self.user.getEmail())
        self.sg = sendgrid.SendGridAPIClient(apikey = "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")

    def sendEmail(self):
        """
        a function that sends an email to the user with his fish farm data
        """
        excel_file = ExcelConverter()
        attachementPath = excel_file.getFilePath(self.user.getUsername(), self.user.getPassword())
        subject = "Fish Farm Data."
        body = Content("text/plain", "Attached below is a file containing your Fish Farm data.")
        with open(attachementPath, 'rb') as fd:
             b64data = base64.b64encode(fd.read())
        attachment = Attachment()
        attachment.content = str(b64data,'utf-8')
        attachment.filename = "Data"
        self.message = Mail(self.sender, subject, self.recipient, body)
        self.message.add_attachment(attachment)
        response = self.sg.client.mail.send.post(request_body=self.message.get())
        print("Email sent")
