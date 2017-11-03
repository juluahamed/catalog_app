from django.conf.urls import url
from wasp import views
urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'^newcategory', views.newCategory, name='newcategory'),
    url(r'^newitem', views.newItem, name='newitem'),
    url(r'^(?P<id>[0-9]+)/view', views.viewCategory, name='viewcategory'),
    url(r'^(?P<c_id>[0-9]+)/item/(?P<i_id>[0-9]+)/view', views.viewItem, name='viewitem'),
    url(r'^(?P<c_id>[0-9]+)/item/(?P<i_id>[0-9]+)/edit', views.editItem, name='edititem'),
	url(r'^(?P<c_id>[0-9]+)/item/(?P<i_id>[0-9]+)/delete', views.deleteItem, name='deleteitem')    
]