from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user_cart/', views.user_cart, name='user_cart'),
    path('profile/', views.profile_view, name='profile'),
]
