from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


urlpatterns = [
    path('', views.CreateStudent, name='create_student'),
    path('std_detail/<str:reg>/', views.GetStudent, name='std_detail'),
    path('delete/<int:id>', views.DeleteStudent, name='delete'),
]