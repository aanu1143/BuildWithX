from django.urls import path
from .views import HomeView, ProjectCreateView, ProfileDetailView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new_project/', ProjectCreateView.as_view(), name='new_project'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
