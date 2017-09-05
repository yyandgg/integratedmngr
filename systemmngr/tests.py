from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from collections import defaultdict

from .models import Role, Userinfo, Userrole


import logging
logger = logging.getLogger(__name__)
# create your tests here.

class  RoleTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        Role.objects.create(name = 'admin', describes = 'this is a super management.')
        Role.objects.create(name = 'develop', describes = 'this is a clever develop.')
        
    def tearDown(self):
        self.client = None
    
    def test_role_add(self):
        
        response = self.client.post(reverse('role_add'), {'name': 'test', 'describes': 'i am a tester.'})
        print '####start test role add#####'
        print Role.objects.all()
        print response.status_code
        print '####end test role add ######'

    def test_role_list(self):
        response = self.client.get(reverse('role_list'))
        print '####start test role list#####'
        print response.context['roles']
        print '####end test role list#######'

    def test_role_edit(self):
        response  = self.client.post(reverse('role_edit', kwargs={'role_id': 1}), {'name': 'test', 'describes': 'i am a tester.'})
        print '####start test role edit######'
        print Role.objects.get(pk=1).name
        print Role.objects.get(pk=1).describes
        print response.status_code
        print '####end test role edir########'
        
    def test_role_delete(self):
        self.client.post(reverse('role_delete', kwargs={'role_id': 1}))
        print '#####start test role delete####'
        print Role.objects.all()
        print '####end test role delete ######'

class UserTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        Userinfo.objects.create(name='lyy', email='whh@qq.com', password='111111', phone=12322, idcard=1232232, status=1, isfirstlogin=1)

    def tearDown(self):
        self.client = None

    def test_user_list(self):
        response = self.client.get(reverse('user_list'))
         
        print '#### start user list ####'
        print response.context['users']
        print response.status_code
        print '### stop user list ######'

    def test_user_add(self):
        response = self.client.post(reverse('user_add'), {'name':'yy', "email":'hh@qq.com', 'password':'111111', 'phone':12322, 'idcard':1232232, 'status': '1', 'isfirstlogin': 1})
        print '#### start user add ###'
        print Userinfo.objects.all()
        print Userinfo.objects.get(pk=2).password
        print '#### end user add #####'

    def test_user_edit(self):
        response = self.client.post(reverse('user_edit', kwargs={'user_id': 1}), {'name':'yy', "email":'hh@qq.com', 'password':'111111', 'phone':12322, 'idcard':1232232, 'status': '1', 'isfirstlogin': 1})
        print '#### start test user edit #####'
        print Userinfo.objects.get(pk=1).name
        print response.status_code
        print '#### end test user edit #######'

    def test_user_delete(self):
        self.client.post(reverse('user_delete', kwargs={'user_id': 1}))
        print '### start test user delete #####'
        print Userinfo.objects.all()
        print '### end test user delete ######'

class UserRoleTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        Role.objects.create(name = 'admin', describes = 'this is a super management.')
        Role.objects.create(name = 'develop', describes = 'this is a clever develop.')
        Role.objects.create(name = 'test', describes = 'this is a test.')
        Role.objects.create(name = 'product', describes = 'this is a clever product.')


        Userinfo.objects.create(name='lyy', email='whh@qq.com', password='111111', phone=12322, idcard=1232232, status=1, isfirstlogin=1)
        Userinfo.objects.create(name='hh', email='hh@qq.com', password='111111', phone=12322, idcard=1232232, status=1, isfirstlogin=1)
        Userinfo.objects.create(name='ff', email='ff@qq.com', password='111111', phone=12322, idcard=1232232, status=1, isfirstlogin=1)
        
    def tearDown(self):
        self.client = None

    def test_role_menu(self):
        response = self.client.get(reverse('role_menu'))
        print '##### test role menu #######'
        print response.context['roles']
        print '#######end test role menu ##########'

    def test_user_role_save_req_post(self):
        data = defaultdict(list)
        data['roles'] = {"2": [1, 3]}
        reponse = self.client.post(reverse('user_role_save'), data)

    def test_user_role_list_req(self):
        Userrole.objects.create(roleid=1, userid=2)
        Userrole.objects.create(roleid=1, userid=3)
        Userrole.objects.create(roleid=3, userid=2)
        Userrole.objects.create(roleid=2, userid=1)
        Userrole.objects.create(roleid=2, userid=3)
    
        response = self.client.get(reverse('user_role_list', kwargs={'role_id': 3}))
        print '##### start user role list req #####'
        print response.context['users_role']
        for i in response.context['users_role']:
            print i.checked
        print '##### end user role list req #######'



