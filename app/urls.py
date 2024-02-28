from django.urls import path
from . import views
urlpatterns = [
    path('',views.create,name='create'),
    path('retrive/',views.retrive,name='retrive'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),



]
