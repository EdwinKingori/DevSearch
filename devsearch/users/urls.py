from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.userprofile, name="user-profile"),
    path('account/', views.userAccount, name="account"),
    path('edit_account', views.editAccount, name='edit-account')

]
