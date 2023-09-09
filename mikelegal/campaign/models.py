from django.db import models
from django.core.mail import EmailMessage

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email

class Campaign(models.Model):
    subject = models.CharField(max_length=200)
    preview_text = models.TextField()
    article_url = models.URLField()
    html_content = models.TextField()
    plain_text_content = models.TextField()
    published_date = models.DateField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    
    def send_email(self):
        email = EmailMessage(
            subject=self.subject,
            body=self.plain_text_content,
            from_email='your_email@example.com',
            to=['subscriber1@example.com', 'subscriber2@example.com'],
        )
        email.send()
        self.sent = True
        self.save()
