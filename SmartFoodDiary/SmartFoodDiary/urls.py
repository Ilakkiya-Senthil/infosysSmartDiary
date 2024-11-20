# smartfooddiary/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('users.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Ensure 'users' is the correct path prefix
    path('accounts/', include('allauth.urls')),
]