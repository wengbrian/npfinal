from django import forms
from django.utils.safestring import mark_safe

class RegForm(forms.Form):
    account = forms.EmailField(label=mark_safe('Email'), widget=forms.TextInput(attrs={'class':'fill_form'}))
    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'fill_form'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'fill_form'}), min_length=6)

class LoginForm(forms.Form):
	account = forms.EmailField(label=mark_safe('Email'), widget=forms.TextInput(attrs={'class':'fill_form'}))	
	password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'fill_form'}), min_length=6)