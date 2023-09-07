
from django.urls import path


from.import views

#here we going to views using path and function
urlpatterns = [

    path('',views.demo,name='demo'),

    # path('add/',views.addition,name='addition')
   # path('about/',views.about,name='about'),
    #path('contact/',view.contact,name='contact')
]