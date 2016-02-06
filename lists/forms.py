from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Item

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob',)


class ItemForm(forms.Form):
    item = forms.CharField(
        label="",  # To turn off label
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Add Item',
                'autofocus': 'true'
            })
    )
