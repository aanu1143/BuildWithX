from django.urls import path
from .views import HomeView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectDetail
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new_project/', ProjectCreateView.as_view(), name='new_project'),
    path('<int:pk>/', ProjectUpdateView.as_view(), name='edit_project'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('<int:pk>/detail',ProjectDetail, name='project_detail'),
]
