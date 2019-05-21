from django import forms
from . models import Food, Item, User

class FoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['category', 'cover']


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['category', 'name', 'restaurant', 'location']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
