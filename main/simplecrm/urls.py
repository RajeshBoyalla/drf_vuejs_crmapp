"""simplecrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from crmapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/accounts', views.AccountAPIView.as_view(), name='account-list'),
    path(r'api/contacts', views.ContactAPIView.as_view(), name='contact-list'),
    path(r'api/activities', views.ActivityAPIView.as_view(), name='activity-list'),
    path(r'api/activitystatuses', views.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path(r'api/contactsources', views.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path(r'api/contactstatuses', views.ContactStatusAPIView.as_view(), name='contact-status-list'),
    path('', TemplateView.as_view(template_name='crmapp/index.html')),
]
