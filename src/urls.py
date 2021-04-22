from django.contrib import admin
from django.urls import path
from ecommerce.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name="main"),
    path('<str:title>', individualPage, name="product"),
    path('pay/<int:id>', payPage, name="payPage")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)