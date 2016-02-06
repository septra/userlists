from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from models import User, Item
from .forms import UserForm, ItemForm

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = slugify(form.cleaned_data['name'])
            return redirect('/users/%s/' % user_name)
    else:
        form = UserForm()
    return render(request, 'lists/home.html', {'form':form})


def list_view(request, user_name):
    user = User.objects.get_or_create(
                user_name = user_name,
                name= " ".join(map(str.capitalize, str(user_name).split('-')))
    )[0]

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item.objects.create(text=form.cleaned_data['item'], user=user)
            return redirect('/users/%s/' % user.user_name)
    else:
        form = ItemForm()
        list_items = Item.objects.filter(user=user)
    context = {
                'user':user,
                'form':form
    }
    return render(request, 'lists/list.html', context)
