from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('update_task/<str:primary_key>/', views.UpdateTask.as_view(), name='update_task')
]
