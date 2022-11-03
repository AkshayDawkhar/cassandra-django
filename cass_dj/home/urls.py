from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homes,name='home'),
    path('a',views.hoemapi,name='homeapi')
]
