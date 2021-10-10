from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


#Register router here 
router = DefaultRouter()
router.register('', views.StudentView, basename="StudenView")



urlpatterns = [
    path('api/', include(router.urls)),
]
