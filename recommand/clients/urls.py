from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index),

    # path('signup/', views.signUp, name='signup'),
    # path('login/', views.Login, name='login'),
    # path('logout/', views.Logout, name='logout'),
    # path('<int:movie_id>/', views.detail, name='detail'),
    # path('watch/', views.watch, name='watch'),
    # path('recommend/', views.recommend, name='recommend'),
    # path('Action/',views.Action,name='Action'),
    # path('Adventure/', views.Adventure, name='Adventure'),
   
]