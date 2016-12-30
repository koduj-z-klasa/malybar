from django.conf.urls import url
from . import views  # import widoków aplikacji

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
