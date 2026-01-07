from django.urls import path
from django import views
from .views import Users,User,ActivateAccount,UserListForAdmin,SingleUserListForAdmin

urlpatterns = [
    path('users',Users.as_view(),name="users"),
    path('user/<int:pk>',User.as_view(),name="user"),
    path('admin/users',UserListForAdmin.as_view(),name="users-for-admin"),
    path('admin/user/<int:pk>',SingleUserListForAdmin.as_view(),name="single-user-for-admin"),
    path("activate/<uidb64>/<token>/",ActivateAccount.as_view(),name="activate-account"),


    # path('create',create_user,name="createUser")
]



