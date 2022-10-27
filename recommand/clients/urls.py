import tempfile
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("index/", views.index),
  #  path("finduser/<user>",views.getUser)
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('uploadImg/<int:oid>/', tempfile.uploadImg),

    # path('signup/', views.signUp, name='signup'),
    # path('login/', views.Login, name='login'),
    # path('logout/', views.Logout, name='logout'),
    # path('<int:movie_id>/', views.detail, name='detail'),
    # path('watch/', views.watch, name='watch'),
    # path('recommend/', views.recommend, name='recommend'),
    # path('Action/',views.Action,name='Action'),
    # path('Adventure/', views.Adventure, name='Adventure'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)