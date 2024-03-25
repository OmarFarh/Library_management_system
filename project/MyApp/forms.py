from django import forms
from .models import *


class Book_Add(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'Title',
            'Auther_Name',
            'Book_Photo',
            'Auther_Photo',
            'Pages',
            'Price',
            'States',
            'category',
        ]

        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'Auther_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Book_Photo': forms.FileInput(attrs={'class':'form-control'}),
            'Auther_Photo': forms.FileInput(attrs={'class':'form-control'}),
            'Pages': forms.NumberInput(attrs={'class':'form-control'}),
            'Price': forms.NumberInput(attrs={'class':'form-control'}),
            'States': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }

class Cat_Add(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }