from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        return redirect('/users/%s/' % request.POST['user_name'].replace(' ', '-').lower())
    return render(request, 'lists/home.html')

def user_list(request, name):
    context = {'user':name}
    return render(request, 'lists/list.html', context)
