from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^index.html$', views.post_list, name='index'),
    url(r'^login.html$', views.login, name='login'),
    url(r'^register.html$', views.register, name='register'),
]