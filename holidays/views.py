from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import *
from .parser import get_holidays, get_countrys
from .models import Holiday


class HolidayView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        holidays = Holiday.objects.filter(
            country=request.user.userprofile.country
        )
        serializer = HolidaySerializer(holidays, many=True)
        return Response({'data': serializer.data})


class SaveHolidaysView(APIView):
    permission_classes = [permissions.IsAdminUser]

    @staticmethod
    def post(request):
        Holiday.objects.all().delete()
        for country in get_countrys():
            for i in get_holidays(country):
                holiday = Holiday()
                holiday.country = str(country).replace('\xa0','')
                holiday.name = i[0]
                holiday.date = i[1]
                holiday.save()
        return Response({'ok': True})
