# TODO There's certainly more than one way to do this task, so take your pick.


from rest_framework import serializers
from apps.demo.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username")

    class Meta:
        model = Comment
        fields = ["text", "timestamp", "author"]

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username")
    comment_count = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "text", "timestamp", "author", "comment_count", "comments"]

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        comments = obj.comments.all().order_by("-timestamp")[:3]
        return CommentSerializer(comments, many=True).data
