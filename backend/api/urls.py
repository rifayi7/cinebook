from django.urls import path
from django import views
from .views import index

urlpatterns = [
    path('',index.as_view(),name="index"),
    # path('create',create_user,name="createUser")
]

