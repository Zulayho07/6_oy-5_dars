from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Car, Brand
from .forms import CarForm, BrandForm


def home(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()

    context = {
        'brands': brands,
        'cars': cars,
        'title': 'Mashinalar'
    }
    return render(request, 'main/index.html', context)


def car_detail(request, car_id):
    brands = Brand.objects.all()
    car = Car.objects.get(id=car_id)
    context = {
        'brands': brands,
        'car': car,
        'title': car.model
    }
    return render(request, 'main/detail.html', context)


def car_by_brand(request, brand_id):
    brands = Brand.objects.all()
    brand = Brand.objects.get(id=brand_id)
    cars = Car.objects.filter(brand_id=brand_id)

    context = {
        'brands': brands,
        'brand_id': brand.id,
        'cars': cars,
        'title': brand.title
    }
    return render(request, 'main/index.html', context)


def add_car(request: HttpRequest):
    if request.method == 'POST':
        form = CarForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            car = form.save()
            return redirect('detail', car_id=car.pk)
    form = CarForm()
    context = {
        'form': form
    }
    return render(request, "main/add_car.html", context)


def add_brand(request: HttpRequest):
    if request.method == 'POST':
        form = BrandForm(data=request.POST)
        if form.is_valid():
            brand = form.save()
            return redirect('car_by_brand', brand_id=brand.pk)
    form=BrandForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_brand.html', context)
