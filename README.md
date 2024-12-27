Django Restful, PDF, Gaston Hillar 
12/27/2024

chp8b pg237 wip adding default user to drone table (model)

#users
python manage.py createsuperuser
hal:hal

#url
http://localhost:8000/drones
#upto chp4
http://localhost:8000/toys

#Surface Bookpro PyCharm
projects\Django\Gaston_Hillar\restful

#github
https://github.com/PacktPublishing/Django-RESTful-Web-Services

#commands
python manage.py runserver
.\projects\venvDjango3\Scripts\activate
.\venvDjango3\Scripts\activate

chp6
python manage.py startapp drones
python manage.py makemigrations drones #233

#notes
serializers:
    1. class Meta: model and especially the "fields".
    2. properties: allows constraints and name rendering.
          a. property of other serializer class thru id of foreign key.
          b. property of other serializer class thru another model's related name.
                serializers.HyperlinkedRelatedField.
          c. property of other serializer class thru other model of foreign key.
          e. property thru serializers.SlugRelatedField(queryset=<Model name>.objects.all(), slug_field='description').
                slugfield <Model name> field is display.
    3. serializers.HyperlinkedModelSerializer: makes url.
    4. Model that does not have related name will not be shown in the parent model.

/*
We also have to pay special attention to the relationships between the different models when we
create the serializer classes to manage serialization to JSON and deserialization from JSON.
*/

debug steps:
  urls has views class
  views class has serializer class
  serializer class has model class under class Meta
