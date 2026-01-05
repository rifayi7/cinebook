from django.urls import path
from django import views
from .views import Users,User

urlpatterns = [
    path('users',Users.as_view(),name="users"),
    path('user/<int:pk>',User.as_view(),name="user"),
    # path('create',create_user,name="createUser")
]

