from rest_framework import permissions #chp8
from drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication #chp8
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
from drones.serializers import DroneCategorySerializer, CompetitionSerializer, CompetitionPilotSerializer
from drones.serializers import DroneSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer

#url(r'^drone-categories/$')
class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'

#url(r'^drone-categories/(?P<pk>[0-9]+)$')
class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    lookup_field = 'pk'
    name = 'dronecategory-detail'

#url(r'^drones/$')
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'

#url(r'^drones/(?P<pk>[0-9]+)$'
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'


#url(r'^pilots/$)
class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'

class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'

class CompetitionPilot(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionPilotSerializer
    name = 'competitionPilot'

class Competition(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    name = 'competition'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request)
            })
