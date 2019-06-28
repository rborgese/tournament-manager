from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class AppConfig(AppConfig):
    name = 'app'


class CustomAdminConfig(AdminConfig):
    default_site = 'app.admin.CustomAdminSite'

