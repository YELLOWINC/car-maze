from django import forms
from django.contrib.auth.models import User
from cars.models import UserProfile, Car


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password', 'email',)


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('district', 'gender', 'DOB')


class SearchForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('manufacturer', 'type')