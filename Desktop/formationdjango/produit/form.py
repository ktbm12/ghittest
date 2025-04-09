from django import forms
from .models import produit

class produitForm(forms.ModelForm):
    price = forms.FloatField()
    class Meta:
        model = produit
        fields = ['name', 'price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super(produitForm, self).__init__(*args, **kwargs)
            self.fields['name'].label = 'Nom du produit'
            self.fields['price'].label = 'Prix du produit'
            self.fields['description'].label = 'Description du produit'
            self.fields['image'].label = 'Image du produit'
            
            
            # forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)
