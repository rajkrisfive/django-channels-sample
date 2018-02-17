from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channel.consumers import DemoConsumer


application = ProtocolTypeRouter({
"websocket": AuthMiddlewareStack(
        URLRouter([
            # URLRouter just takes standard Django path() or url() entries.
            path("channel/demo/", DemoConsumer),
        ]),
)
})