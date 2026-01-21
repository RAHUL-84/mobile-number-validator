from django.urls import path
from .views import validate_mobile, home

urlpatterns = [
    path('', home, name='home'),  # home page
    path('validate_mobile/', validate_mobile, name='validate_mobile'),
]
