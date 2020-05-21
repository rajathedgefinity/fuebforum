from django.urls import path
from community import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_forum, name='login'),
    # path('post-login/', views.post_login, name='post-login'),
    path('faq/', views.faq, name='faq'),
    path('forum-thread/', views.forum_thread, name='forum_thread'),
    path('profile/', views.profile, name='profile'),
    path('profile-settings/', views.profile_settings, name='profile_settings'),
    path('logout/', views.logout_user, name='logout'),
]
