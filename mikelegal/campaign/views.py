
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Campaign, Subscriber
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def add_subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        Subscriber.objects.create(email=email, first_name=first_name)
        return redirect('add-subscriber')

    return render(request, 'add_subscriber.html')

def mark_inactive(request, subscriber_id):
    subscriber = Subscriber.objects.get(id=subscriber_id)
    
    if request.method == 'POST':
        subscriber.is_active = False
        subscriber.save()
        return redirect('add-subscriber')
    
    return render(request, 'mark_inactive.html', {'subscriber': subscriber})

def list_subscribers(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'list_subscribers.html', {'subscribers': subscribers})


def create_campaign(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        preview_text = request.POST['preview_text']
        article_url = request.POST['article_url']
        html_content = request.POST['html_content']
        plain_text_content = request.POST['plain_text_content']
        published_date = request.POST['published_date']

        Campaign.objects.create(
            subject=subject,
            preview_text=preview_text,
            article_url=article_url,
            html_content=html_content,
            plain_text_content=plain_text_content,
            published_date=published_date
        )

        messages.success(request, 'Campaign created successfully') 

    campaigns = Campaign.objects.all()

    return render(request, 'create_campaign.html', {'campaigns': campaigns})

def send_email(request, campaign_id):
    try:
        campaign = Campaign.objects.get(id=campaign_id)
        subject = campaign.subject
        html_content = campaign.html_content
        active_subscribers = Subscriber.objects.filter(subscribed=True)
        email_recipients = [subscriber.email for subscriber in active_subscribers]
        send_email_to_recipients(subject, html_content, email_recipients)

        messages.success(request, f'Email sent for campaign: {campaign.subject}')
    except Campaign.DoesNotExist:
        messages.error(request, 'Campaign not found.')

    return redirect('create-campaign')


def send_email_to_recipients(subject, html_content, recipients):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'gabbarsingh1907@gmail.com'
    smtp_password = 'huct byhq gngi ojpo'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    for recipient in recipients:
        msg = MIMEMultipart('alternative')
        msg['From'] = smtp_username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(html_content, 'html'))

        server.sendmail(smtp_username, recipient, msg.as_string())

    server.quit()