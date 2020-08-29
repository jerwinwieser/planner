from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create_person/', views.PersonCreateView.as_view(), name='create_person'),
    path('update_person/<int:pk>', views.PersonUpdateView.as_view(), name='update_person'),
    path('delete_person/<int:pk>', views.PersonDeleteView.as_view(), name='delete_person'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
	path('rest/', views.data_rest_api, name='data_rest_api'),
	path('serial/', views.data_rest_api_serial, name='data_rest_api_serial'),
]

