from django import forms

from .models import Userinfo, Role

class LoginForm(forms.Form):
    
    class Meta:
        model = Userinfo
        widgets = {
            'password': forms.PasswordInput(),
        },
        fields = ('email', 'password', )

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Userinfo
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = ('name', 'email', 'password', 'phone', 'idcard', 'status', 'isfirstlogin', )
        
class RoleForm(forms.ModelForm):
    
    class Meta:
        model = Role
        fields = ('name', 'describes', )
