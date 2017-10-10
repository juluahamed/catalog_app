from django.conf.urls import url
from wasp import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
