from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^login', views.showLogin, name='login'),
    url(r'^logout', views.logout, name='logout')

]