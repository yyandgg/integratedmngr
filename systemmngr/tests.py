from django.test import TestCase, Client

from .models import Role

from django.core.urlresolvers import reverse
# create your tests here.

class  RoleTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        
    def tearDown(self):
        self.client = None
    
    def test_role_add(self):
        
        response = self.client.post(reverse('role_add'), {'name': 'test', 'describes': 'i am a tester.'})
        print Role.objects.all()
        print response.status_code

    def test_role_list(self):
        response = self.client.get(reverse('role_list'))
        print Role.objects.all()
        print response.context['roles']
        
