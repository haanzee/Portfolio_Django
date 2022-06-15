from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index_View, name='index'),
    path('skills/', views.Skills_View, name='skills'),
    path('profile/', views.Profile_View, name='profile'),
    path('projects/', views.Projects_View, name='projects'),
    path('projectdet/', views.ProjectDetails_View, name='projectdet'),
    path('certifications/', views.Certification_View, name='certifications'),
    path('resume/', views.Resume_View, name='resume'),
]

