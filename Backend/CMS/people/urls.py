from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('person/', views.people, name='people'),
    path('person/<str:pk>', views.person, name='person'),
    path('list', views.PeopleListView.as_view(), name='list'),
]