from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path("register/", include("register.urls")),
        path("admin/", admin.tresagilecom.urls).
        ]
