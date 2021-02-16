import os
from celery import Celery

from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrueHome.settings')

app = Celery('TrueHome')
#app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')
#app.autodiscover_tasks()
app.autodiscover_tasks(settings.INSTALLED_APPS)