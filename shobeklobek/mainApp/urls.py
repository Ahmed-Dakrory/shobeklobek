from django.urls import path
from . import views 
from .import context_processor_file

app_name = 'mainApp'

urlpatterns = [
    path('',views.loadMainPage,name = 'loadMainPage'),
    # path('about',views.loadAboutPage,name = 'loadAboutPage'),

]
