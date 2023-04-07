from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('my_collections/<int:pk>', views.MyCollectionsView.as_view(), name='my_collections'),
]


