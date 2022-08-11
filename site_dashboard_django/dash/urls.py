from django.urls import path

from . import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
    path('dashboard/', views.index, name='index'),
    path('dashboard/projects/', views.projects, name='projects'),
    path('dashboard/projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('dashboard/userstory/<int:us_id>/', views.us_detail, name='us_detail'),
    path('dashboard/about', views.about, name='about'),
]