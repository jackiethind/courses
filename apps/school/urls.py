from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    # url(r'^comments_process$', views.comments_process),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^comments/(?P<id>\d+)$', views.comments),

]
