from django.urls import path, include
from fa import views

urlpatterns = [
    path('' ,views.index ,name ='index'),
]
