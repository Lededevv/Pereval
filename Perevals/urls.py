from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from peaks.views import PerevalViewSet

router = routers.SimpleRouter()
router.register(r'perevals', PerevalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
