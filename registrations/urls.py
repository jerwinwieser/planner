from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.PersonCreateView.as_view(), name='person_create'),
    path('read/<int:pk>', views.PersonReadView.as_view(), name='person_read'),
    path('update/<int:pk>', views.PersonUpdateView.as_view(), name='person_update'),
    path('delete/<int:pk>', views.PersonDeleteView.as_view(), name='person_delete'),
    path('tables/', views.tables, name='tables'),
    path('charts/', views.charts, name='charts'),
	path('rest/', views.data_rest_api, name='data_rest_api'),
	path('serial/', views.data_rest_api_serial, name='data_rest_api_serial'),
]

