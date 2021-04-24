from django.contrib import admin
from django.urls import path
from ecommerce.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage, name="main"),
    path('pay/<int:amount>/<str:user>', payPage, name="payPage"),
    path('pay/<str:order_id>', payPage2, name="payPage2")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)