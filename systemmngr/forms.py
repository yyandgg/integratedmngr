from django import forms

from .models import Userinfo

class UserForm(forms.ModelForm):
    
    class Meta:
        model = Userinfo
        widgets = {
        'password': forms.PasswordInput(),
        }
        fields = ('email', 'password', )
        
