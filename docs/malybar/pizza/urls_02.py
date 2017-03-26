from django.conf.urls import url
from . import views  # import widoków aplikacji
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Pizza

app_name = 'pizza'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', login_required(ListView.as_view(model=Pizza)),
        name='lista'),
]
