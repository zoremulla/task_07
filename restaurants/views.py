from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def restaurant_update(request, restaurant_id):
    rest=Restaurant.objects.get(restaurant_id)
    form=RestaurantForm(instance=restaurant_id)
    if request.method=='POST':
        form=Restaurant(request.POST, instance=rest)
        if form.is_valid():
            form.save()

            return redirect('restaurant-list')
    context={
        'rest':rest,
        'form':form,
    }
    
    return render(request, 'update.html', context)

def restaurant_delete(request, restaurant_id):
    Restaurant.objects.get(id=restaurant_id).delete()


    return redirect('restaurant-list')
