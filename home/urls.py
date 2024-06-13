from django.urls import path
from . import views

urlpatterns = [
    
    path('men', views.men_view, name='men'),
    path('women', views.women_view, name='women'),
    path('kids', views.kids, name='kids'),
    path('men<int:men_id>/', views.product, name='product'),
    path('kid<int:kid_id>/', views.kidproduct, name='kidproduct'),
    path('women<int:women_id>/', views.womenproduct, name='womenproduct'),
    path('home', views.home, name='home'),
    # path('<int:men_id>/', views.kidproduct, name='kidproduct'),
        ]
