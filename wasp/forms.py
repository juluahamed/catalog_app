from django import forms
from wasp.models import Category, Item

# Classes for Model Form

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'document')

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('name', 'description', 'category', 'document')
