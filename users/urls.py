from django.urls import path

from .views import UserListView,UserCreateView,UserDetailView,UserUpdateView,UserDeleteView

urlpatterns = [
    path('post/<int:pk>/', UserDetailView.as_view(), name='user_detail'), 
    path('post/new/', UserCreateView.as_view(), name='new_user'),
    path('', UserListView.as_view(), name='home'),
    path('post/<int:pk>/edit/',
        UserUpdateView.as_view(), name='user_edit'),
    path('post/<int:pk>/delete/',UserDeleteView.as_view(), name='user_delete'),
]
