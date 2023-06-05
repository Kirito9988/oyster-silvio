from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('products/', views.products, name='products'),
    path('cost/', views.cost, name='cost'),  # new line
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),  # You will have to create the 'signup' view
    path('start/', views.start, name='start'),
]
