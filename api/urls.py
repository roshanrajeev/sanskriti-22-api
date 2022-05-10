from django.urls import path, include
from .views import EventListApi, EventDetailApi, EventTypeListApi

urlpatterns = [
    path('events/', EventListApi.as_view()),
    path('events/<int:pk>/', EventDetailApi.as_view()),
    path('events/<str:type>/', EventTypeListApi.as_view()),
]
