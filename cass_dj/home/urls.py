from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homes, name='home'),
    path('a', views.hoemapi, name='homeapi'),
    path('b', views.finalapi, name='homeapi2')
]
