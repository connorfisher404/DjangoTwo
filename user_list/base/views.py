from django.shortcuts import render
from .models import List
# Create your views here.

def index(request):
    items = List.objects.all()
    if request.method == 'POST':
        new_item = request.POST.get("add_item")
        List.objects.create(item=new_item)

    return render(request, 'face/index.html',{"items": items})

def delete(request):
    items = List.objects.all()
    if request.method == 'POST':
        delete_item = request.POST.get("delete_item")
        List.objects.filter(item=delete_item).delete()
    return render(request, 'face/delete.html',{"items":items})
