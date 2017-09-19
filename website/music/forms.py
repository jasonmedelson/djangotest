from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField() #to hide password onscreen pass 'widget=forms.PasswordInput'
    class Meta:
        model = User
        fields = ['username', 'email', 'password']