from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('post/<int:id>/like/', views.like_post, name='like_post'),
    path('post/<int:id>/comment/', views.add_comment, name='add_comment'),

    path('profile/<str:username>/', views.profile, name='profile'),

    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
]