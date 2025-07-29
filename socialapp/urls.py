from django.urls import path 
from . import views


urlpatterns = [
    path('',views.Login, name="login-file"),
    path('auth/register/',views.Register, name="register"),
    path('dashboard/socialdashboard', views.social_dashboard, name='socialdashboard'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
