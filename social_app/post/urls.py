from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(), name='post-submit'),
    path('<int:id>/', views.PostView.as_view(), name='post-by_id'),
    path('self/', views.PostSelfView.as_view(), name='post-self'),
    path('delete/<int:id>/', views.delete_post_by_id, name='post-delete_by_id'),
    path('update/<int:id>/', views.update_post_by_id, name='post-update_by_id'),
    path('home/', views.PostFollowersView.as_view(), name='post-home'),
]
