from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
 	path('data/rest/', views.data_rest.as_view(), name='data_rest'),
 	path('chart/', views.render_chart, name='chart'),
 	path('form/', views.render_form, name='form'),
]
