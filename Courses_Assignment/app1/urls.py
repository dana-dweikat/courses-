from django.contrib import admin
from django.urls import path
from . import views 

app_name = 'app1'

urlpatterns = [
    path('',views.home,name='home'),
    path('remove/<str:pk>', views.remove, name='remove'),
    path('destroy/<str:pk>', views.destroy, name='destroy'),
]

