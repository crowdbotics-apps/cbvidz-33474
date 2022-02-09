from django.contrib import admin
import os
from django.urls import path, include

admin_url = os.getenv('ADMIN_URL')
urlpatterns = [
    path("", include("home.urls")),
    path(admin_url + '/admin/', admin.site.urls),
]

admin.site.site_header = "cbvidz"
admin.site.site_title = "cbvidz Admin Portal"
admin.site.index_title = "cbvidz Admin"