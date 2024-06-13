from django.urls import path
from . import views

urlpatterns = [
    path('orderrev', views.orderrevv, name='orderrev'),
        ]
