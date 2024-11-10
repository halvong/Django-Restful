from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('toys.urls')),
]
#path('admin/', admin.site.urls),
