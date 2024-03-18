from django.urls import path,re_path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('',views.index,name='index'),
    re_path(r'^stu$',views.stu),
    re_path(r'^user$',views.user),
    re_path(r'^user\/add_user$',views.add_user),
    re_path(r'^add$',views.add,name='add'),
    re_path(r'^user\/delete_user\/(?P<id>[0-9]+)$',views.delete_user),
    # re_path(r'^user\/edit_user$',views.edit_user),
    re_path(r'^user\/edit_user\/(?P<id>[0-9]+)$',views.edit_user),
    # re_path(r'([0-9]+)\/([0-9]+)',views.plus),
    re_path(r'(?P<num1>[0-9]+)\/(?P<num2>[0-9]+)',views.plus_named),
]













