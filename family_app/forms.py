from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tkinter import Widget
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from .models import *
# Create your forms here.

class NewUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':True,}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':True,}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required':True,}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required':True,}))
    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['username'].empty_label = '--'
        self.fields['email'].empty_label = '--'
        self.fields['password1'].empty_label = '--'
        self.fields['password2'].empty_label = '--'
        
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class Familyform(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required':True,}))
    def __init__(self, *args, **kwargs):
        super(Familyform, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.fields['name'].empty_label = '--'
        self.fields['no_hp'].empty_label = '--'
        self.fields['email'].empty_label = '--'
        self.fields['tgl_lahir'].empty_label = '--'
        self.fields['negara'].empty_label = '--'
        self.fields['kota'].empty_label = '--'
    class Meta:
        model=Family
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'no_hp':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'tgl_lahir':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'negara':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'kota':forms.TextInput(attrs={'class':'form-control','required':True,}),}   