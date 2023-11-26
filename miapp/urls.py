from django.urls import path, include
from rest_framework import routers
from miapp import views
from .views import HitoView

router=routers.DefaultRouter()
router.register(r'hitos', views.HitoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('eventos/', HitoView.as_view(), name='hitos_list'),
    path('eventos/<int:id>', HitoView.as_view(), name='hitos_process')
]
