"""
ASGI config for finca project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import django
from channels.routing import get_default_application
from channels.asgi import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finca.settings')
# django.setup()
# application = get_default_application()

channel_layer = get_channel_layer()