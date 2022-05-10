from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
	path('paginaweb', views.index, name='paginaweb'),
	path('hora', views.current_datetime, name='hora'),
	path('vista', views.vista, name='vista'),
]
