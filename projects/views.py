from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Project
from django.core.exceptions import PermissionDenied
from .forms import ProjectForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Project

    def get_queryset(self):
        search_tag = self.request.GET.get('search','')
        return Project.objects.filter(project_name__contains=search_tag)



class ProjectCreateView(LoginRequiredMixin,CreateView):
   model = Project
   template_name = 'project_new.html'
   form_class = ProjectForm
   login_url = 'login'
   success_url = reverse_lazy('home')

   def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ProjectCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

   def form_valid(self,form): #if form is valid
     form.instance.user = self.request.user
     return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'project_edit.html'
    login_url = 'login'
    success_url = 'profile_project'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
