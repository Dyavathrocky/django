from django.urls import path
from mysite import views

urlpatterns=[
    path('',views.index1,name='index1'),
]
