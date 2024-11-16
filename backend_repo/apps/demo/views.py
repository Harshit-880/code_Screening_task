# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from apps.demo.models import Post
from apps.demo.serializers import PostSerializer

class PostPagination(PageNumberPagination):
    page_size = 5  # Default page size
    page_size_query_param = "page_size"  # Allow clients to set page size via query params
    max_page_size = 100  # Maximum allowed page size

class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by("-timestamp")
    serializer_class = PostSerializer
    pagination_class = PostPagination
