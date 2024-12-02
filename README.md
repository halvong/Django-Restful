Django Restful, PDF, Gaston Hillar 
12/01/2024

chp6 pg171 ends class-based views and generic class

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

#notes
serializers:
    1. class Meta: model and especially the "fields"
    2. properties: allows constraints and name rendering
          a. property of other serializer class thru model id of foreign key
          b. property of other serializer class thru other model's related name
          c. property of other serializer class thru other model of foreign key
          e. property thru SlugRelatedField(queryset=<Model name>.objects.all())
    3. hyperlinked: makes url
    4. SlugRelatedField: render name of a field

    /*If a parent class, one-to-many, does not have a related name in the children class,
       the parent will display children records using the children model name. */

debug steps:
  urls has views class
  views class has serializer class
  serializer class has model class under class Meta
