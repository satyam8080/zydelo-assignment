from django.urls import path
from . import views

urlpatterns = [
    path('', views.FollowingListView.as_view(), name='follow-following_list'),
    path('<int:user_id>/', views.FollowView.as_view(), name='follow-by_id'),
    path('get/', views.FollowListView.as_view(), name='follow-followers_list'),

]
