from django import forms
from django.forms import ModelForm
from .models import Project,types

class ProjectForm(ModelForm):
    website_image = forms.FileField()
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}))
    user_type = forms.ChoiceField(widget=forms.RadioSelect, choices=types)
    class Meta:
        model = Project
        fields = ['project_name','build_with','website_image','url','user_type','description']

