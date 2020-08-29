from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.PersonCreateView.as_view(), name='create_person'),
    path('delete/<int:pk>', views.PersonDeleteView.as_view(), name='delete_person'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
	path('rest/', views.data_rest_api, name='data_rest_api'),
	path('serial/', views.data_rest_api_serial, name='data_rest_api_serial'),
]

