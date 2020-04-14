from django.urls import path
from .views import HomeView, ProjectCreateView, ProjectUpdateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new_project/', ProjectCreateView.as_view(), name='new_project'),
    path('new_project/<int:pk>/', ProjectUpdateView.as_view(), name='edit_project'),
]
