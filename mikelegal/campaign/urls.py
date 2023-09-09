# campaigns/urls.py

from django.urls import path
from .views import add_subscriber, create_campaign, list_subscribers, mark_inactive , send_email

urlpatterns = [
    path('add-subscriber/', add_subscriber, name='add-subscriber'),
    path('mark-inactive/<int:subscriber_id>/', mark_inactive, name='mark-inactive'),
    path('list-subscribers/', list_subscribers, name='list-subscribers'),
    path('create-campaign/', create_campaign, name='create-campaign'),
    path('send_email/<int:campaign_id>/', send_email, name='send_email'),  # Add this line



]
