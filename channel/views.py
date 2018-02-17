from django.http import HttpResponse
from django.views.generic.base import TemplateView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from random import randint
import json

channel_layer = get_channel_layer()


class Home(TemplateView):
    template_name = 'channel/home.html'

    def get(self, request, *args, **kwargs):
        if self.request.is_ajax():
            async_to_sync(channel_layer.group_send)("demo_group",
                                                    {"type": "demo.send", "name": "John Doe",
                                                     "id": randint(1,100)})
            return HttpResponse({'message': "success"})
        return super(Home, self).get(request, *args, **kwargs)

