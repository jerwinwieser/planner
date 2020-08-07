from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('check/', views.check, name='check'),
    path('current_datetime/', views.current_datetime, name='current_datetime'),
    path('redir/', views.redir, name='redir'),
    path('render_404/', views.render_404, name='render_404'),
]