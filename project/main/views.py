from django.shortcuts import render
from .models import Car, Brand


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
        'brands':brands,
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
