from .models import Car, Brand
from django import forms

class CarForm(forms.ModelForm):
    class Meta:
        model= Car
        fields='__all__'
        widgets={
            'model': forms.TextInput(attrs={
                'placeholder': 'Modeli',
                'class': 'form-control',
            }),
            'year': forms.DateInput(attrs={
                'placeholder': 'Yili',
                'class': 'form-control',
            }),
            'transmission':forms.TextInput(attrs={
                'placeholder': 'Tezlik turi',
                'class': 'form-control',
            }),
            'fuel_type':forms.TextInput(attrs={
                'placeholder': 'Yoqilg\'i turi',
                'class': 'form-control',
            }),
            'price':forms.NumberInput(attrs={
                'placeholder': 'Narxi',
                'class': 'form-control',
            }),
            'image':forms.FileInput(attrs={
                'placeholder': 'Rasm',
                'class': 'form-control',
            }),
            'brand':forms.Select(attrs={
                'placeholder': 'Brendi',
                'class': 'form-select',
            })
        }
        labels={
            'model':'Modeli',
            'year':'Yili',
            'transmission':'Tezlik turi',
            'fuel_type':'Yoqilg\'i turi',
            'price':'Narxi',
            'image':'Rasm',
            'brand':'Brendi'
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={
                'placeholder':'Nomi',
                'class': 'form-control'
            }),
            'country': forms.TextInput(attrs={
                'placeholder':'Mamlakat',
                'class':'form-control'
            }),
            'founded_year':forms.DateInput(attrs={
                'placeholder':'Asos solingan yili',
                'class': 'form-control'
            })
        }
        labels={
            'title':'Nomi',
            'country':'Mamlakat',
            'founded_year':'Asos solingan yil'
        }