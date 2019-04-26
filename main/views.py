from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class EventView(APIView):

    @staticmethod
    def get(request):
        events = Event.objects.filter(user=request.user)
        serializer = EventSerializer(events, many=True)
        return Response({'data': serializer.data})

    @staticmethod
    def post(request):
        event = EventSerializer(data=request.data)
        if event.is_valid(raise_exception=True):
            event.save(user=request.user)
            return Response({'ok': True})


class EventDayView(APIView):

    @staticmethod
    def get(request):
        kwargs = dict(user=request.user)
        if request.GET.get('year'):
            kwargs['start_datetime__year'] = request.GET['year']
        if request.GET.get('month'):
            kwargs['start_datetime__month'] = request.GET['month']
        if request.GET.get('day'):
            kwargs['start_datetime__day'] = request.GET['day']
        events = Event.objects.filter(**kwargs)
        serializer = EventSerializer(events, many=True)
        return Response({'data': serializer.data})

