from django.urls import path
from .views import *
urlpatterns = [
    path("check" , MarketingSender.send_message , name="send_message" )
]
