import sendgrid

class emailNotifier():
    def __init__(self, sender, recipient):
        """
        Constructor to the emailNotifier class, takes sender and recipient email addresses
        """
        self.sender = sender
        self.recipient = recipient
        self.client = sendgrid.SendGridClient("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")
        self.message = sendgrid.Mail()

    def sendEmail(self, subject, body):
        """
        a function that takes the subject and the body as input and sends an email
        """
        self.subject = subject
        self.body = body
        self.message.add_to(self.recipient)
        self.message.set_from(self.sender)
        self.message.set_subject(self.subject)
        self.message.set_html(self.body)
        self.client.send(self.message)

em = emailNotifier("madeinalexmia@gmail.com","abdullahsalah96@outlook.com")
em.sendEmail("hi", "from SendGrid")
