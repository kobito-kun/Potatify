from django.contrib import admin
from django.urls import path
from ecommerce.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name="main"),
]
