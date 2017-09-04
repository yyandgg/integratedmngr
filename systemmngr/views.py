import md5
import hashlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .forms import UserForm
from .models import Userinfo


# Create your views here.
def index(request):
    
    content = cache.get('user')
    context = {
        'username': content
    }
    print context
    print 'index view'
    return render(request, 'pages/home.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_form = UserForm({'email': email, 'password': password})
        if user_form.is_valid():
            try:
                password_md5 = hashlib.md5(user_form.cleaned_data['password']).hexdigest()
                user = Userinfo.objects.get(email=user_form.cleaned_data['email'], password=password_md5)
                cache.set('user', email)
                return HttpResponseRedirect(reverse('homepage'))
            except Userinfo.DoesNotExist:
                raise Http404("No Userinfo matches the given query.")
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        user_form = UserForm()
        context = {
            'form': user_form
        }
        return render(request, 'pages/login.html', context)

def loginout(request):
    cache.delete('user')
    return HttpResponseRedirect(reverse('homepage'))
    
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_form = UserForm({'email': email, 'password': password})
        if user_form.is_valid():
            password_md5 = hashlib.md5(user_form.cleaned_data['password']).hexdigest()
            Userinfo.objects.create(email=user_form.cleaned_data['email'], password=password_md5)
            cache.set('user', email)
            return HttpResponseRedirect(reverse('homepage'))
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        user_form = UserForm()
        context = {
            'form': user_form
        }
        return render(request, 'pages/register.html', context)
