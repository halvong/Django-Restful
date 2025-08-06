from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('drones.urls')),
    url('^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')) #p234
]

#url(r'^', include('toys.urls')),  # regular expression works for url position
