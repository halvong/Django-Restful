Django Restful, PDF, Gaston Hillar 
8/05/2025

chp8 Reviewing API
urls,py, views.py, serializers.py, models.py

chp8 Authentication & Permissions starts
pg209


#users
python manage.py createsuperuser
hal:hal

#url
#upto chp4
http://localhost:8000/toys
http://localhost:8000/drones

chp7: http ":8000/drone-categories/?name=Quadcopter"
http://localhost:8000/drones/?search=G
http://localhost:8000/drones/?drone_category=1&has_it_competed=false&ordering=-name
http://localhost:8000/competitions/?min_distance_in_feet=700&max_distance_in_feet=9000&from_achievement_date=2017-10-18&to_achievement_date=2017-10-22&ordering=-achievement_date

#Surface Bookpro PyCharm Postgresql restful
projects\Django\Gaston_Hillar\restful

#github
https://github.com/PacktPublishing/Django-RESTful-Web-Services

#commands
python manage.py runserver
.\projects\venvDjango3\Scripts\activate
.\venvDjango3\Scripts\activate

#chp6
python manage.py startapp drones
python manage.py makemigrations drones #233
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
  hal:hal

#notes
https://www.cdrf.co

1. serializers - representation of JSON output (model -> serializer -> JSON):
    A. class Meta has model and fields properties
    B. Serializer attribute is a nested serializer of another model.
       a. HyperlinkedModelSerializer - hyperlinked url.
       b. SlugRelatedField - specify name for related data
       c. Slugfield renders name of a field
          serializers.SlugRelatedField(queryset=<Model name>.objects.all(), slug_field='description').
          "description" field is chosen to display.
    C. related field - pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')# Display pilot name
       related json fields - pilot = PilotSerializer()

2. models - representation of form POST
    A. ForeignKey property: allows constraints and name rendering.
          a. foreign key is related data from other model.
          b. related name is handler is for parent serializer. Use SlugRelatedField on Serializer to display name.
          c. no related name in foreign key cannot be access from the parent model.
    B. models.py class fields display as input box in Django REST framework.

3. filter_fields - don't know what it does

/*
We also have to pay special attention to the relationships between the different models when we
create the serializer classes to manage serialization to JSON and deserialization from JSON.
*/
The correct import in Views.py is like this:
from django_filters import rest_framework as filters
and the code for CompetitionFilteris like this
min_distance_in_feet = filters.NumberFilter( field_name='distance_in_feet', lookup_expr='gte') max_distance_in_feet = filters.NumberFilter( field_name='distance_in_feet', lookup_expr='lte')

debug steps:
  urls has views class
  views class has serializer class
  serializer class has model class under class Meta

#
docker exec -it f8ca45 bash
 psql -U postgres
 postgres

 ----
