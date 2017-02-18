from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^complete_delete/(?P<id>\d+)$', views.complete_delete),

]
