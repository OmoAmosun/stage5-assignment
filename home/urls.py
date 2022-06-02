from django.urls import path
from home.views import home, about, contact


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact)
]