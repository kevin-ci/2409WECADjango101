from django import forms
from .models import List, Item

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'image', 'description', 'creator']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity']