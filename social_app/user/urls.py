from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='user-registration'),
    path('<int:id>/', views.get_user_profile, name='user-registration'),
]
