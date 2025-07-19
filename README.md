Django Restful, PDF, Gaston Hillar 
7/18/2025

chp6 reviewing Generic ListCreateAPIView

#old
chp8c pg252 wip token-based authentication not working

#users
python manage.py createsuperuser
hal:hal

#url
http://localhost:8000/drones
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

serializers - represent model as a JSON object (model -> serializer -> JSON):
    1. class Meta has model and fields properties
    2. foreign key property: allows constraints and name rendering.
          a. foreign key is related data from other model.
          b. related name is handler for parent model. Use SlugRelatedField on Serializer to display name.
          c. no related name in foreign key cannot be access from the parent model.
    3. Serializer HyperlinkedModelSerializer makes hyperlinked url.
    4. Serializer attribute is a nested serializer of another model.
    5. Slugfield renders name of a field
          serializers.SlugRelatedField(queryset=<Model name>.objects.all(), slug_field='description').
          "description" field is chosen to display.

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