from django.urls import path,re_path
from . import views
# from django.conf.urls import url

urlpatterns = [
    # re_path(r'^/(?P<pIndex>[0-9]+)$',views.vote_info,name='vote_info'),
    path('',views.vote_info,name='vote_info'),
    path('display_user_info',views.display_user_vote,name='display_user_info'),
    path('login',views.Login.as_view(),name='login'),
    # path('logout',views.Logout.as_view(),name='logout'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.Register.as_view(),name='register'),
    re_path(r'^add_vote$',views.add_vote,name='add_vote'),
    re_path(r'^edit_vote\/(?P<id>[0-9]+)$',views.edit_vote,name='edit_vote'),
    re_path(r'^delete_vote\/(?P<id>[0-9]+)$',views.delete_vote),
]













