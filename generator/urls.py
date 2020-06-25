from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'generator'

urlpatterns = [
    path('generator', views.home, name = 'homepage'),
    path('password/', views.password, name = 'password'),
    path('about/', views.about, name = 'about' ),
]
