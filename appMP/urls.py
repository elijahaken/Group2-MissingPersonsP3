from django.urls import path
from .views import MissingPersonsTable, personView

#these paths will take you to either the landingpage or the individual persons page.
urlpatterns = [
    # path('', homeView, name="homePage"),
    path("", MissingPersonsTable, name="index"),
    path('person/<str:personId>', personView, name="personView"),
]