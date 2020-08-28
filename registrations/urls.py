from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('cards/', views.cards, name='cards'),
 	path('form/', views.form_render, name='form_render'),
 	path('edit/<person_id>', views.form_edit, name='form_edit'),
 	path('delete/<person_id>', views.form_delete, name='form_delete'),
	path('rest/', views.data_rest_api, name='data_rest_api'),
	path('serial/', views.data_rest_api_serial, name='data_rest_api_serial'),
]

