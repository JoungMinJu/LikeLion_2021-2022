from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('',showmain,name='main'),
    path('showsecond/',showsecond,name='second'),
    path('showfirst/',showfirst,name='first'),
    path('<str:id>',detail,name='detail'),
    path('new/',new,name='new'),
    path('create/',create,name='create'),
    path('edit/<str:id>',edit,name='edit'),
    path('update/<str:id>',update,name='update'),
    path('delete/<str:id>', delete, name='delete'),

    ]