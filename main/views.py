from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class EventView(APIView):

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        event = EventSerializer(data=request.data)
        if event.is_valid():
            event.save(user=request.user)
            return Response("Add")