from django.urls import path
from .views import PostsView

app_name='quiz'

urlpatterns = [
    path('posts/', PostsView.as_view(), name='posts_view'),   
]