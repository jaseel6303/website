from django.urls import path , include
from . import views

urlpatterns = [
    
    path('', views.index, name='portfolio'),
    path('project_1', views.project_1, name='project_1'),
    path('about', views.about,name='about'),
    path('booking', views.booking,name='booking'),
    path('doctors', views.doctors,name='doctors'),
    path('contact', views.contact,name='contact'),
    path('department', views.department,name='department'),

]