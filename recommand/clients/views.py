import sys
sys.path.append('../')
sys.path.append('../wrec')
from http.client import HTTPResponse
from django.shortcuts import render
from. import models
from .models import Wallpaper ,User ,Rating
import json
from django.db.models import Q
#from . import collectuser
# from .collectuser import niu

# Create your views here.

# def index(request):
#         name_list = ['id','imagNAME', 'imagSRC', 'imagTAGS']
#         return render(request, 'index.html', {'List': json.dumps(name_list )})

def index(request):
    wallpaper = Wallpaper.objects.all()
    user = User.objects.all()
    rating = Rating.objects.all()
    query = request.GET.get('q')
    a = Wallpaper(imagNAME = 'test1',)
    b = User(username = 'test2',)
    c = Rating(rating = 'test3',)
   # a.save()
    print(a)
    print(b)
    print(c)
    print(len(wallpaper))
    print(len(user))
    print(len(rating))
    

    if query:
        wallpaper = wallpaper.objects.filter(Q(title__icontains=query)).distinct()
        return render(request, 'index.html', {'wallpaper': wallpaper})

    return render(request, 'index.html', {'wallpaper': wallpaper})


def uploadImg(request,oid):
    objs = models.Img.objects.filter(project_id_id=oid)
    if request.method == "POST":
        obj = models.Order.objects.get(id=oid)
        if request.FILES.get('img') is None:
            return render(request, "imgUpload.html", {"imgs": objs})
        img = models.Img(img_url=request.FILES.get('img'),project_id=obj)
        img.save()
    return render(request, "imgUpload.html",{"imgs":objs})



'''
def getUser(request,name):
    return niu(name)'''
     




# def index(request):
#     wallpaper=models.Acticle.objects.get(pk=1)
#     return render(request, 'index.html', {"wallpaper": wallpaper}) 


    
# def index(request):
#     if request.method == 'GET':
#         index = request.GET.get('index')
#         return render(request, 'index.html', locals())   
        


