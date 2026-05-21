import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import voice_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assistant_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            voice_app.routing.websocket_urlpatterns
        )
    ),
})