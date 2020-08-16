from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
 	path('rest/', views.data_rest, name='data_rest'),
 	path('chart/', views.render_chart, name='chart'),
 	path('form/', views.render_form, name='form'),
 	path('delete/<person_id>', views.delete, name='delete'),
 	path('edit/<person_id>', views.edit, name='edit'),
]







# urlpatterns = [
#     path('', views.index, name='index'),
#  	# path('rest/<int:pk>/', views.data_rest, name='data_rest'),
#  	path('chart/', views.render_chart, name='chart'),
#  	path('form/', views.render_form, name='form'),
#  	path('delete/<person_id>', views.delete, name='delete'),
#  	path('edit/<person_id>', views.edit, name='edit'),
# ]



