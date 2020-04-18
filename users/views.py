from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import CustomUserCreationForm, UserForm, UpdateProfile
from .models import CustomUser
from projects.models import Project
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
    form_class = UpdateProfile

class ProfileDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    form_class = UserForm
    template_name = 'profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['page']='detail'
        return context

class ProfileAboutView(LoginRequiredMixin,DetailView):
    model = CustomUser
    form_class = UserForm
    template_name = 'profile_about.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileAboutView, self).get_context_data(**kwargs)
        context['page']= 'about'
        return context


class ProfileProjectView(LoginRequiredMixin, ListView):
  model = Project
  template_name = 'profile_project.html'

  def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
