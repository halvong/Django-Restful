"""
chp 6
"""
from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
import drones.views

""" 
POST returns data
{
    "url": "http://localhost:8000/drone-categories/1",
    "pk": 1,
    "name": "Fixed-wing",
    "drones": []
}
GET one example from many
{
    "url": "http://localhost:8000/drone-categories/1",
    "pk": 1,
    "name": "Fixed-wing",
    "drones": [
        "http://localhost:8000/drones/5",
        "http://localhost:8000/drones/2",
        "http://localhost:8000/drones/3",
        "http://localhost:8000/drones/4"
    ]
}
"""
class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
	#HyperlinkedRelatedField: Drone model's drones is a related_name
	drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')

	class Meta:
		model = DroneCategory #id,name
		fields = ('url', 'pk', 'name', 'drones') #POST

""" POST returns
{
    "url": "http://localhost:8000/drones/1",
    "name": "Scout AI",
    "drone_category": "Single-rotor",
    "manufacturing_date": "2024-08-26T01:15:00",
    "has_it_competed": true,
    "inserted_timestamp": "2024-11-29T22:18:11.925009"
}

"drone_category": [
   "Object with name=fixed does not exist."
]
"""
class DroneSerializer(serializers.HyperlinkedModelSerializer):
	#display the category name, SlugRelatedField: dronecategory must exists constraint
	drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

	class Meta:
		model = Drone
		fields = ('url', 'name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp')

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
	# Display all the details for the related drone
	drone = DroneSerializer()

	class Meta:
		model = Competition
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'drone')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
	competitions = CompetitionSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
	gender_description = serializers.CharField(source='get_gender_display', read_only=True)

	class Meta:
		model = Pilot
		fields = ('url', 'name', 'gender', 'gender_description', 'races_count', 'inserted_timestamp', 'competitions')

class PilotCompetitionSerializer(serializers.ModelSerializer):
	pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')# Display pilot name
	drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')# Display drone name

	class Meta:
		model = Competition
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'pilot', 'drone')


