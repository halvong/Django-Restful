Django Restful, PDF, Gaston Hillar 
8/04/2025

chp7 filtering, searching, ordering
     p194

#old
chp8c pg252 wip token-based authentication not working

#users
python manage.py createsuperuser
hal:hal

#url
http://localhost:8000/drones
chp7: http ":8000/drone-categories/?name=Quadcopter"
#upto chp4
http://localhost:8000/toys

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
/*
We also have to pay special attention to the relationships between the different models when we
create the serializer classes to manage serialization to JSON and deserialization from JSON.
*/

debug steps:
  urls has views class
  views class has serializer class
  serializer class has model class under class Meta

#
docker exec -it f8ca45 bash
 psql -U postgres
 postgres

 ----
