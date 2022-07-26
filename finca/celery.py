import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finca.settings")

app = Celery("finca",
            broker="amqp://celery_user:celery@localhost:5672/celery_host",
    )

app.config_from_object("django.conf:settings", namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# from __future__ import absolute_import

# import os

# from celery import Celery

# from django.conf import settings

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finca.settings")

# app = Celery('finca')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
