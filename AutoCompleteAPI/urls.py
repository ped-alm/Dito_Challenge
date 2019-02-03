from rest_framework import routers
from .views import UserViewSet, EventDataViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/eventsData', EventDataViewSet)

urlpatterns = [
    path('', include(router.urls))
]
