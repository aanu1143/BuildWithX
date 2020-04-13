from django.urls import path
from .views import SignUpView, ProfileDetailView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
