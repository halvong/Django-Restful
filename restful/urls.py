from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('drones.urls')),
]
#path('admin/', admin.site.urls),
#url(r'^', include('toys.urls')),  # regular expression works for url position
