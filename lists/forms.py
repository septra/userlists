from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Item

def render_widget(widget, placeholder=None, autofocus='false'):
    attrs={
        'class':'form-control input-lg',
        'placeholder':placeholder,
        'autofocus':autofocus,
        'autocomplete': 'off'
    }
    return widget(attrs)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
        widgets = {
                'username': render_widget(forms.TextInput, 'Username', 'true'),
                'first_name': render_widget(forms.TextInput, 'First Name'),
                'last_name': render_widget(forms.TextInput, 'Last Name'),
                'email': render_widget(forms.EmailInput, 'Email'),
                'password': forms.PasswordInput(
                        attrs={
                            'class':'form-control input-lg',
                            'placeholder':'Password'
                        })
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob',)
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs = {
                    #'class':'form-control'
                },
                years = range(1950, 2016)
            )
        }
        labels = {
            'dob': 'Date of Birth'
        }


class ItemForm(forms.Form):
    item = forms.CharField(
        label="",  # To turn off label
        max_length=100,
        widget = render_widget(forms.TextInput, 'Add Item', 'true')
    )
