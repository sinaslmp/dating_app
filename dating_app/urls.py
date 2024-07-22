from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/matches/', include('matches.urls')),
    path('api/messages/', include('user_messages.urls')),
    path('api/notifications/', include('notifications.urls')),
]
