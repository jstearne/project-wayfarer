from django.urls import path
from . import views

urlpatterns = [
    #path for home page
    path('', views.Home.as_view(), name="home"), 
    #path for profile page 
    path('profile/', views.Profile.as_view(), name="profile"),
    
    #path for single post about a park page
    #need to come back to update route
    path('posts/', views.Post.as_view(), name="posts"),
    #path to login- might need to update route later
    path('login/', views.Login.as_view(), name="login"),
    #path for user to sign-up/register
    path('signup/', views.Signup.as_view(), name="signup"),
    
]