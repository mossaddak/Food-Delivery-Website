from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('Login/', views.Login, name='Login'),
    path('SingUp/', views.SingUp, name='SingUp'),
    path('Logout/', views.Logout, name="Logout"),
    path('ForgetPassword/', views.ForgetPassword, name="ForgetPassword"),
    path('ChangePassword/<token>/', views.ChangePassword, name="ChangePassword"),
    path('UserProfile/', views.UserProfile, name='UserProfile'),
    path('ChangeProfilePicture/', views.ChangeProfilePicture, name='ChangeProfilePicture'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path('facebook/social-auth/', include('social_django.urls', namespace='social'))
    path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    

]
  