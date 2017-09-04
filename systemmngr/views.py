import md5
import hashlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .forms import UserForm, RoleForm
from .models import Userinfo, Role


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

def role_list(request):
    roles = Role.objects.all()
    context = {
        'roles': roles
    }
    return render(request, 'pages/role_list.html', context)

def role_add(request):
    if request.method == 'POST':
        role_form = RoleForm(request.POST)
        if role_form.is_valid():
            print role_form.cleaned_data
            Role.objects.create(name=role_form.cleaned_data['name'], describes=role_form.cleaned_data['describes'])
            return HttpResponseRedirect(reverse('role_list'))
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        role_form = RoleForm()
        context = {
            'form': role_form
        }
        return render(request, 'pages/role_add.html', context)

def role_edit(request, role_id):

    role = Role.objects.get(pk=role_id)

    if request.method == 'POST':
        role_form = RoleForm(request.POST)
        if role_form.is_valid():
            
            role.name = role_form.cleaned_data['name']
            role.describes = role_form.cleaned_data['describes']
            role.save()
            return HttpResponseRedirect(reverse('role_list'))
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        role_form = RoleForm(instance=role)
        context = {
            'form': role_form
        }
        return render(request, 'pages/role_edit.html', context)

def role_delete(request, role_id):
    Role.objects.get(pk=role_id).delete()
    return HttpResponseRedirect(reverse('role_list'))
 
               
