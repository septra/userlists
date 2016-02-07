from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from models import UserProfile, Item
from .forms import UserForm, ItemForm, UserProfileForm

from django.core.cache import cache

# Create your views here.
class HomeView(TemplateView):
    template_name = "lists/home.html"

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('/')
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'lists/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            UserProfile.objects.get(user__username = username)
        except:
            messages.error(
                    request,
                    'Please <a href="/signup">register</a> to login'
            )
            return redirect('/login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, "You've been successfully logged in!")
                return redirect('/%s/' % username)
            else:
                return HttpResponse('Your account is not active')
        else:
            messages.error(request, "Incorrect login details")
            return redirect('/login')
    else:
        return render(request, 'lists/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def list_view(request, user_name):

    if request.user.username != user_name:
        return redirect('/')

    user = get_object_or_404(UserProfile, user__username=user_name)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            Item.objects.create(text=form.cleaned_data['item'], userprofile=user)
            items = Item.objects.filter(userprofile=user)
            cache.set(user, items)
            return redirect('/%s' % user_name)
    else:
        form = ItemForm()
        if cache.get(user):
            list_items = cache.get(user)
        else:
            list_items = Item.objects.filter(userprofile=user)
            cache.set(user, list_items)

    context = {
                'user':user,
                'form':form
    }
    return render(request, 'lists/list.html', context)
