from django.urls import path

from . import views

# here we going to views using path and function
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
