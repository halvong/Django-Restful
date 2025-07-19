"""
chp 6
"""
from django.contrib.auth.models import User
from rest_framework import serializers
from drones.models import DroneCategory
from drones.models import Drone
from drones.models import Pilot
from drones.models import Competition

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
	#model's related_name and hyperlinked url, orderby in models
	drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')

	class Meta:
		model = DroneCategory #id,name
		fields = ('pk', 'name', 'url', 'drones') #POST,GET drones from Drone will display

class DroneSerializer(serializers.HyperlinkedModelSerializer):
	#display the category name, POST SlugRelatedField: dronecategory must exists constraint
	#thru SlugRelatedField(queryset= <Model name>.objects.all())
	drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(), slug_field='name')

	class Meta:
		model = Drone #id, name, drone_category_id, manufacturing_date, has_it_competed, inserted_timestamp
		fields = ('id','name', 'drone_category', 'url', 'manufacturing_date', 'has_it_competed', 'inserted_timestamp')

class PilotCompetitionSerializer(serializers.ModelSerializer):
	#display related pilot and drone names
	pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')# Display pilot name
	drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')# Display drone name

	class Meta:
		model = Competition #id, distance_in_feet, distance_achievement_date, drone_id, pilot_id
		#rendering
		fields = ('id', 'distance_in_feet', 'distance_achievement_date', 'url', 'pilot', 'drone')

#similiar to CompetitionPilotSerializer
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
	# Display all the details for the related drone
	# thru model id of foreign key
	drone = DroneSerializer()

	class Meta:
		model = Competition #id, distance_in_feet,distance_achievement_date, drone_id, pilot_id
		fields = ('id', 'distance_in_feet', 'distance_achievement_date', 'url', 'drone')

class PilotSerializer(serializers.HyperlinkedModelSerializer):
	#class thru other model of foreign key (pilot_id)
	competitions = CompetitionSerializer(many=True, read_only=True)
	gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES) #constraint M, F
	#render gender description instead of char pg155 Male, Female
	gender_description = serializers.CharField(source='get_gender_display', read_only=True)

	class Meta:
		model = Pilot #id, name, gender, races_count, inserted_timestamp
		#rendering
		fields = ('id', 'name', 'gender', 'gender_description', 'races_count', 'inserted_timestamp', 'url', 'competitions')

#similiar to CompetitionSerializer w/o pilot property
#url(r'^competition-pilot/$')
class CompetitionPilotSerializer(serializers.HyperlinkedModelSerializer):
	#thru model id of foreign key
	drone = DroneSerializer()
	pilot = PilotSerializer()

	class Meta:
		model = Competition #id, distance_in_feet,distance_achievement_date, drone_id, pilot_id
		fields = ('url', 'pk', 'distance_in_feet', 'distance_achievement_date', 'pilot_id', 'pilot', 'drone_id', 'drone')


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Drone
		fields = ( 'url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	drones = UserDroneSerializer(many=True, read_only=True) #drone model related_name

	class Meta:
		model = User
		fields = ( 'url', 'pk', 'username', 'drone')