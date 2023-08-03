from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('api/person/', views.people, name='people'),
    path('api/person/<str:pk>', views.person, name='person'),
    path('api/list', views.PeopleListView.as_view(), name='list'),
]