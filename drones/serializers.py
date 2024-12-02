"""
chp 6
"""
from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition
""" 
class Meta: model and fields
propertes: allows constraints and custom rendering
hyperlinked: makes url 
SlugRelatedField: render name of a field

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
	#GET HyperlinkedRelatedField gives url link
	#thru other model's related name
	drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')

	class Meta:
		model = DroneCategory #id,name
		fields = ('url', 'pk', 'name', 'drones') #POST,GET drones from Drone will display

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
	#display the category name, POST SlugRelatedField: dronecategory must exists constraint
	#thru SlugRelatedField(queryset= <Model name>.objects.all())
	drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

	class Meta:
		model = Drone #id, name, drone_category_id, manufacturing_date, has_it_competed, inserted_timestamp
		fields = ('url', 'name', 'drone_category', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp')

class PilotCompetitionSerializer(serializers.ModelSerializer):
	'''
	offers constraints in POST pilot and drone
    "pilot": [ "Object with name=Peter Perfect does not exist." ],
    "drone": [ "Object with name=Scout does not exist." ]
	'''
	#display corresponding pilot and drone names
	#thru SlugRelatedField(queryset= <Model name>.objects.all())
	pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')# Display pilot name
	drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')# Display drone name

	class Meta:
		model = Competition #id, distance_in_feet, distance_achievement_date, drone_id, pilot_id
		#rendering
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'pilot', 'drone')

#similiar to CompetitionPilotSerializer
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
	# Display all the details for the related drone
	# thru model id of foreign key
	drone = DroneSerializer()

	class Meta:
		model = Competition #id, distance_in_feet,distance_achievement_date, drone_id, pilot_id
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'drone')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
	#class thru other model of foreign key (pilot_id)
	competitions = CompetitionSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES) #constraint M, F
	#render gender description instead of char pg155 Male, Female
	gender_description = serializers.CharField(source='get_gender_display', read_only=True)

	class Meta:
		model = Pilot #id, name, gender, races_count, inserted_timestamp
		#rendering
		fields = ('url', 'name', 'gender', 'gender_description', 'races_count', 'inserted_timestamp', 'competitions')

#similiar to CompetitionSerializer w/o pilot property
#url(r'^competition-pilot/$')
class CompetitionPilotSerializer(serializers.HyperlinkedModelSerializer):
	#thru model id of foreign key
	drone = DroneSerializer()
	pilot = PilotSerializer()

	class Meta:
		model = Competition #id, distance_in_feet,distance_achievement_date, drone_id, pilot_id
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'pilot_id', 'pilot', 'drone_id', 'drone')
