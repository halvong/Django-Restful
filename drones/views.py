from rest_framework import permissions #chp8
from drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication #chp8
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import rest_framework as filters, AllValuesFilter, DateTimeFilter, NumberFilter
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
from drones.serializers import DroneCategorySerializer, CompetitionSerializer, CompetitionPilotSerializer
from drones.serializers import DroneSerializer
from drones.serializers import PilotSerializer
from drones.serializers import PilotCompetitionSerializer

#url(r'^drone-categories/$') okay
class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)
    name = 'dronecategory-list'

#url(r'^drone-categories/(?P<pk>[0-9]+)$') okay
class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    lookup_field = 'pk'
    name = 'dronecategory-detail'

#http://localhost:8000/drones/?drone_category=1&has_it_competed=False&ordering=-name
#url(r'^drones/$') okay
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    filter_fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_competed',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'manufacturing_date',)
    name = 'drone-list'

#url(r'^drones/(?P<pk>[0-9]+)$') okay
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'

#url(r'^pilots/$') okay
class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    filter_fields = ('name', 'gender', 'races_count',)
    search_fields = ('^name',)
    ordering_fields = ('name', 'races_count',)
    name = 'pilot-list'

#url(r'^pilots/(?P<pk>[0-9]+)$')
class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    lookup_field = 'pk'
    name = 'pilot-detail'

class CompetitionFilter(filters.FilterSet):
    from_achievement_date = DateTimeFilter(name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = DateTimeFilter(name='distance_achievement_date', lookup_expr='lte')
    min_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='gte')
    max_distance_in_feet = NumberFilter(field_name='distance_in_feet', lookup_expr='lte')
    drone_name = AllValuesFilter(name='drone__name')
    pilot_name = AllValuesFilter(name='pilot__name')

    class Meta:
        model = Competition
        fields = ('distance_in_feet', 'from_achievement_date', 'to_achievement_date', 'min_distance_in_feet', 'max_distance_in_feet', 'pilot_name', )

#url(r'^competitions/$')
class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    filter_class = CompetitionFilter
    ordering_fields = ('distance_in_feet', 'distance_achievement_date')
    name = 'competition-list'

#url(r'^competitions/(?P<pk>[0-9]+)$')
class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    lookup_field = 'pk'
    name = 'competition-detail'

class CompetitionPilot(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionPilotSerializer
    name = 'competitionPilot'

#url(r'^competition/$')
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
