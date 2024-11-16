from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),  # Existing API routes
    path('admin/', admin.site.urls),  # Add this line for admin access
    path('demo/', include('apps.demo.urls')),
]