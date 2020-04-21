from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .forms import CustomUserCreationForm, UserForm, UpdateProfile
from .models import CustomUser
from projects.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)

class UserUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    template_name = 'user_update.html'
    form_class = UpdateProfile

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'pk': self.request.user.id})

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object():
            raise PermissionDenied
        return super().get(request, *args, **kwargs)


class ProfileDetailView(DetailView):
    model = CustomUser
    form_class = UserForm
    template_name = 'profile_detail.html'

    def get_context_data(self, **kwargs):
        user = kwargs['object']
        ProjectData = Project.objects.filter(user=user)
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['projects_build'] =  ProjectData.filter(user_type='developer')
        context['projects_found'] = ProjectData.filter(user_type='finder')
        return context
