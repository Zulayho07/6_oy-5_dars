from django.urls import path
from .views import home, car_detail, car_by_brand


urlpatterns=[
    path('', home, name='home'),
    path('cars/<int:car_id>/', car_detail, name='detail'),
    path('brands/<int:brand_id>/', car_by_brand, name='car_by_brand'),
]