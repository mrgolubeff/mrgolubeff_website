from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("resources/", include("resources.urls")),
    path('admin/', admin.site.urls),
]
