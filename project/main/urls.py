from django.urls import path
from .views import home, car_detail, car_by_brand, add_car, add_brand


urlpatterns=[
    path('', home, name='home'),
    path('cars/<int:car_id>/', car_detail, name='detail'),
    path('cars/add/', add_car, name='add_car'),
    path('brands/<int:brand_id>/', car_by_brand, name='car_by_brand'),
    path('brands/add/', add_brand, name='add_brand')
]