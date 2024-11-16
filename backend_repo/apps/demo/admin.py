from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'timestamp')  # Display ID, Username, and Timestamp
    list_filter = ('user', 'timestamp')  # Optional: Filter by user and timestamp

    def user_name(self, obj):
        return obj.user.username  # Fetch the username of the user
    user_name.short_description = 'User'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'post_user_name', 'timestamp')  # Display ID, Comment Username, Post Username, and Timestamp
    list_filter = ('user', 'post', 'timestamp')  # Optional: Filter by user, post, and timestamp

    def user_name(self, obj):
        return obj.user.username  # Fetch the username of the user
    user_name.short_description = 'Comment User'

    def post_user_name(self, obj):
        return obj.post.user.username  # Fetch the username of the post's user
    post_user_name.short_description = 'Post User'
