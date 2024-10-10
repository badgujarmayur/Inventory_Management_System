from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryInfoForm
from django.http import HttpResponseRedirect

# Create your views here.


def All_Material(request):
    inventory = Inventory.objects.all()
    return render(request,'All_Material.html',{"Inventory":inventory})


def Update(request, id):
    inventory = get_object_or_404(Inventory, pk=id)
    
    if request.method == 'POST':
        obj = InventoryInfoForm(request.POST, instance=inventory)
        if obj.is_valid():
            obj.save() 
            return HttpResponseRedirect("/")  
    else:
        obj = InventoryInfoForm(instance=inventory)
    
    return render(request, 'update.html', {"form": obj})


def Delete(request, id):
    if request.method == 'POST':
        inventory = Inventory.objects.get(pk=id)
        inventory.delete()
        return HttpResponseRedirect("/")


def Add(request):
    if request.method == 'POST':
        obj = InventoryInfoForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('/') 
    else:
        obj = InventoryInfoForm() 

    return render(request, 'add.html', {"form": obj})