Django Restful, PDF, Gaston Hillar 
11/08/2024

chp3 pg63

#Surface Bookpro VSC
projects\Django\Gaston_Hillar\restful

#commands
python manage.py runserver
.\projects\venvDjango3\Scripts\activate
.\venvDjango3\Scripts\activate

#shells, p54
from datetime import datetime
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer