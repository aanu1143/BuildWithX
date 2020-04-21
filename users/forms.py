from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser, GENDER_CHOICES
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',
                  'contact_number', 'bio', 'image','site_url', 'dob', 'gender')
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class CustomUserChangeForm(UserChangeForm):
    gender = forms.ChoiceField(
            widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',
                  'contact_number', 'bio', 'site_url', 'dob', 'gender')
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CustomUser, self).__init__(*args, **kwargs)


class UpdateProfile(ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','image', 'email',
                  'contact_number', 'bio', 'site_url', 'dob', 'gender')
        labels = {
            'dob': ('D.O.B'),
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }
