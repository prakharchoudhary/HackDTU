from django.conf.urls import url
from . import views

app_name = "BMR"

urlpatterns = [
	url(r'^details/$', views.details, name="details"),
]

