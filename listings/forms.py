from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'price', 'category', 'city', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان الإعلان'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'وصف المنتج أو الخدمة...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السعر (XAF)'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "المدينة (مثلاً: N'Djamena)"}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
