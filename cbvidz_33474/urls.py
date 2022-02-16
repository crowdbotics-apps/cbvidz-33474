from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("", include("home.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "vidzzz"
admin.site.site_title = "vidzzz Admin Portal"
admin.site.index_title = "vidzzz Admin"
