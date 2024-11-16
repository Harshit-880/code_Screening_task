from django.urls import path
from apps.demo.views import PostListView

urlpatterns = [
    path("api/posts/", PostListView.as_view(), name="post-list"),
]