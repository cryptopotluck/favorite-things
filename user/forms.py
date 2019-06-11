from django import forms
from django.contrib.auth.models import User
from .models import Users


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class FirstNameUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        first_name = forms.CharField(required=False)
        fields = ['first_name']


class LastNameUpdateFrom(forms.ModelForm):
    class Meta:
        model = Users
        last_name = forms.CharField(required=False)
        fields = ['last_name']



class ProfilePictureUpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        # profile_image = forms.FileInput()
        fields = ['profile_image']


