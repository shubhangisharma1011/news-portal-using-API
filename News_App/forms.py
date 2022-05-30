from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Profile

#Code Here

class CreateUserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    class Meta:
        model = CustomUser
        fields = ['email','first_name','last_name','address','phone','file']


class UpdatedProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','address','phone','file']