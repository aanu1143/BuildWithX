from django.urls import path
from .views import SignUpView, ProfileDetailView, UserUpdateView, ProfileAboutView, ProfileProjectView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/<int:pk>/', UserUpdateView.as_view(),name='update'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile/about/<int:pk>/',
         ProfileAboutView.as_view(), name='profile_about'),
    path('profile/project/<int:pk>/',
         ProfileProjectView.as_view(), name='profile_project'),
]
