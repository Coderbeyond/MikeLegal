from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('campaign/', include('campaign.urls')),
    path('', RedirectView.as_view(url='/campaign/add-subscriber/', permanent=False), name='root'),
]
