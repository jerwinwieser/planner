from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
 	path('rest/', views.data_rest_api, name='data_rest_api'),
 	path('chart/', views.chart_render, name='chart_render'),
 	path('form/', views.form_render, name='form_render'),
 	path('edit/<person_id>', views.form_edit, name='form_edit'),
 	path('delete/<person_id>', views.form_delete, name='form_delete'),
]

