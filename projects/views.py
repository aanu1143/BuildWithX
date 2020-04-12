from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Project
from users.models import CustomUser

# Create your views here.
class HomeView(ListView):
    template_name = 'home.html'
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
   model = Project
   template_name = 'project_new.html'
   fields = ['project_name','description', 'build_with', 'url', 'website_image', 'user', 'user_type']
   login_url = 'login'

   def form_valid(self,form): #if form is valid
     form.instance.person = self.request.user
     return super().form_valid(form)

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name = 'profile_detail.html'