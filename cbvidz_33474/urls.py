from django.contrib import admin
import os
from django.urls import path, include


urlpatterns = [
    path("", include("home.urls")),
    path(os.getenv('ADMIN_URL')+"/admin/", admin.site.urls),
]

admin.site.site_header = "cbvidz"
admin.site.site_title = "cbvidz Admin Portal"
admin.site.index_title = "cbvidz Admin"