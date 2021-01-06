from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.update, name='update_task'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('api-auth/', include('rest_framework.urls')),
]
