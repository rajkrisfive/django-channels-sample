import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class DemoConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("demo_group", self.channel_name)
        self.accept()

    def demo_send(self, content):
        self.send(json.dumps(content))