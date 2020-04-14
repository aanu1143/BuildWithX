from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import CustomUserCreationForm, UserForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

class UserUpdateView(UpdateView):
    model = CustomUser
    success_url = reverse_lazy('home')
    template_name = 'user_update.html'
    fields = ['username','bio','image'] #You can also create form in forms.py and use it here instead of this step

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    form_class = UserForm
    template_name = 'profile_detail.html'