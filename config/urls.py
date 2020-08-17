from django.contrib import admin
from django.urls import path, include
from obj.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Car', CarViewSet)
router.register(r'Travels', ViagemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls) ),
]
