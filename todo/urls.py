from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Authentication
    path('signup/', views.signupuser, name = "signupuser"),
    path('logout/', views.logoutuser, name = "logoutuser"),
    path('login/', views.loginuser, name = "loginuser"),


    #Actual site
    path('create/', views.createtodo, name = "createtodo"),
    path('current/', views.currenttodos, name = "currenttodos"),
    path('completed/', views.completedtodos, name = "completedtodos"),
    path('todo', views.home, name = "hometodo"),
    path('todo/<int:todo_pk>', views.viewtodo, name = "viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name = "completetodo"),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name = "deletetodo"),

]
