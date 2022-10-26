from http.client import HTTPResponse
from django.shortcuts import render
from. import models
import json
from django.db.models import Q
# Create your views here.

# def index(request):
#         name_list = ['id','imagNAME', 'imagSRC', 'imagTAGS']
#         return render(request, 'index.html', {'List': json.dumps(name_list )})

def index(request):
    wallpaper = wallpaper.objects.all()
    query = request.GET.get('q')

    if query:
        wallpaper = wallpaper.objects.filter(Q(title__icontains=query)).distinct()
        return render(request, 'index.html', {'wallpaper': wallpaper})

    return render(request, 'index.html', {'wallpaper': wallpaper})




# def index(request):
#     wallpaper=models.Acticle.objects.get(pk=1)
#     return render(request, 'index.html', {"wallpaper": wallpaper}) 


    
# def index(request):
#     if request.method == 'GET':
#         index = request.GET.get('index')
#         return render(request, 'index.html', locals())   
        


