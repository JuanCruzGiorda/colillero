from django.urls import path
from .views import ColillasViewSet, ColilleroViewSet,RegistroDatosArduino
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('colillas', ColillasViewSet, basename='colillas')
router.register('colillero', ColilleroViewSet, basename='colillero')
router.register('registro_estados', RegistroDatosArduino, basename='registro_estados')
urlpatterns = router.urls