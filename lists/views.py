from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from models import User, Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        user_name = slugify(request.POST['user_name'])
        return redirect('/users/%s/' % user_name)
    return render(request, 'lists/home.html')


def list_view(request, user_name):

    user = User.objects.get_or_create(
                user_name = user_name,
                name= " ".join(map(str.capitalize, str(user_name).split('-')))
    )[0]

    if request.method == 'POST':
        item = Item.objects.create(text=request.POST['item_input'], user=user)
        return redirect('/users/%s/' % user.user_name)

    list_items = Item.objects.filter(user=user)
    context = {
                'user':user
    }
    return render(request, 'lists/list.html', context)
