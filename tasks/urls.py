from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<str:id>/', views.updateTask, name='update'),
    path('delete/<str:id>/', views.deleteTask, name='delete')
]
