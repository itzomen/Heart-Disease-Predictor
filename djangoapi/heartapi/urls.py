from django.urls import path
from .views import PostsView
from django.conf.urls.static import sta

app_name='quiz'

urlpatterns = [
    path('posts', PostsView.as_view(), name='posts_view'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)