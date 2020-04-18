from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Framework
from django.core.exceptions import PermissionDenied
from .forms import ProjectForm
from django.urls import reverse_lazy


class HomeView(ListView):
    template_name = 'home.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['framworks'] = Framework.objects.all()
        return context

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
    fields = ('project_name', 'description', 'url', 'website_image', 'build_with')
    template_name = 'project_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'project_delete.html'
    login_url = 'login'

    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          projectid = self.kwargs['pk']
          return reverse_lazy('profile_project', kwargs={'pk': projectid})

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'project_detail.html'
    login_url = 'login'
