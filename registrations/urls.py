from django.urls import path

from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
	path('data/json/', views.data_json, name='data_json'),
 	path('data/rest/', views.data_rest.as_view(), name='data_rest'),
 	path('data/chart/', views.data_chart, name='chart'),
]
