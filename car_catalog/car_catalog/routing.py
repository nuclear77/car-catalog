from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import car_api.consumers


application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            car_api.consumers.ChatConsumer.as_asgi(),
        )
    ),
})