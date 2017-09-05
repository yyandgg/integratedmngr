import md5
import hashlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from .forms import LoginForm, UserForm, RoleForm
from .models import Userinfo, Role, Userrole
from .utils import gen_role_related_user

import logging
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    
    content = cache.get('user')
    context = {
        'username': content
    }
    return render(request, 'pages/home.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        login_form = LoginForm({'email': email, 'password': password})
        if login_form.is_valid():
            try:
                password_md5 = hashlib.md5(login_form.cleaned_data['password']).hexdigest()
                user = Userinfo.objects.get(email=login_form.cleaned_data['email'], password=password_md5)  
                cache.set('user', email)
                return HttpResponseRedirect(reverse('homepage'))
            except Userinfo.DoesNotExist:
                raise Http404("No Userinfo matches the given query.")
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        login_form = LoginForm()
        context = {
            'form': login_form
        }
        return render(request, 'pages/login.html', context)

def loginout(request):
    cache.delete('user')
    return HttpResponseRedirect(reverse('homepage'))
    
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        login_form = LoginForm({'email': email, 'password': password})
        if login_form.is_valid():
            password_md5 = hashlib.md5(login_form.cleaned_data['password']).hexdigest()
            Userinfo.objects.create(email=login_form.cleaned_data['email'], password=password_md5)
            cache.set('user', email)
            return HttpResponseRedirect(reverse('homepage'))
        return HttpResponseBadRequest('Invalid Image Request')
    else:
        login_form = LoginForm()
        context = {
            'form': login_form
        }
        return render(request, 'pages/register.html', context)

def user_list(request):
    users = Userinfo.objects.all()
    context = {
        'users': users
    }
    return render(request, 'pages/user_list.html', context)

def user_add(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            password_md5 = hashlib.md5(user_form.cleaned_data['password']).hexdigest()
            Userinfo.objects.create(
                name = user_form.cleaned_data['name'],
                email = user_form.cleaned_data['email'],
                password = password_md5,
                phone = user_form.cleaned_data['phone'],
                idcard = user_form.cleaned_data['idcard'],
                status = user_form.cleaned_data['status'],
                isfirstlogin = user_form.cleaned_data['isfirstlogin']
            )
            return HttpResponseRedirect(reverse('user_list'))
        return HttpResponseBadRequest('Invalid Input Request.')
    else:
        user_form = UserForm()
        context = {
            'form': user_form
        }
        return render(request, 'pages/user_add.html', context)


def user_edit(request, user_id):
    logger.info("hello, world")
    user =  Userinfo.objects.get(pk=user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user.name = user_form.cleaned_data['name']
            user.email = user_form.cleaned_data['email']
            user.phone = user_form.cleaned_data['phone']
            user.idcard = user_form.cleaned_data['idcard']
            user.status = user_form.cleaned_data['status']
            user.isfirstlogin = user_form.cleaned_data['isfirstlogin']
            user.save()
            return HttpResponseRedirect(reverse('user_list'))
        return HttpResponseBadRequest('Invalid input Request.')
    else:
        user_form = UserForm(instance=user)
        context = {
            'form': user_form
        }
        return render(request, 'pages/user_edit.html', context)

def user_delete(request, user_id):
    Userinfo.objects.get(pk=user_id).delete()
    return HttpResponseRedirect(reverse('user_list'))        

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

    role = Role.objects.get(pk=int(role_id))

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

def role_menu(request):
    roles = Role.objects.order_by('createtime')
    context = {
        "roles": roles
    }
    return render(request, 'pages/user_role.html', context)

def user_role_list_req(request, role_id):
    # cha xun chu role fen bie dui ying de ren wu id 
    users = Userinfo.objects.all()
    users_role = Userrole.objects.filter(roleid=role_id)
    print users
    print users_role
    role_related_user = gen_role_related_user(users, users_role)
    context = {
        'users_role': role_related_user
    }
    return render(request, 'pages/special_user.html', context)

def user_role_save_req_post(request):
    data = request.POST
    data['roles'] = {"2": [1, 3], '1': [2, 3], '3': '4'}
    print data
    for roleid, userids in data['roles'].items():
        Userrole.objects.filter(roleid=roleid).delete()
        for userid in userids:
            Userrole.objects.create(userid=int(userid), roleid=int(roleid))  
                
    print Userrole.objects.all()
    
    content = 'create success.'
    return HttpResponse(content)

    

               
