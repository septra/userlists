from django import forms


class UserForm(forms.Form):
    name = forms.CharField(
        label="",  # To turn off label
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Your name'
            })
    )


class ItemForm(forms.Form):
    item = forms.CharField(
        label="",  # To turn off label
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Add Item'
            })
    )
