from django import forms

from .models import Userinfo, Role

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Userinfo
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = ('email', 'password', )
        
class RoleForm(forms.ModelForm):
    
    class Meta:
        model = Role
        fields = ('name', 'describes', )
