from django.urls import path
from .views import HomeView, ProjectCreateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new_project/', ProjectCreateView.as_view(), name='new_project'),
]
