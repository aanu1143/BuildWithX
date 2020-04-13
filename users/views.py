from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, UserForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    form_class = UserForm
    template_name = 'profile_detail.html'