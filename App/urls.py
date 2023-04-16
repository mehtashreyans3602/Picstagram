from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home,name='home'),
    path('', views.login, name='login'),
    path('register',views.registration, name='register'),
    path('logout', views.logoutUser, name="logout"),
    path('user_profile',views.profile, name='user_profile'),
    path('edit-profile', views.edit_profile, name='edit-profile'),
    path('post', views.addPost, name='post'),
    path('user-detail',views.userDetail, name='user-detail'),
]
