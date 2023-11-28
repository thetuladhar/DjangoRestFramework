from django.urls import path
from .views import PersonListView

urlpatterns = [
    path('persons/', PersonListView.as_view(), name='person-list'),
]
