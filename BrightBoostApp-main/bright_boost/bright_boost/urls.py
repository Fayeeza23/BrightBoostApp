from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
     path('', include('brightBoostApp.urls')),  # Include your app's URLs
    path('admin/', admin.site.urls),
    # ... other URL patterns for your project ...
]

# During development, you can serve static files with the Django development server.
# This should be used for debugging only, not in production.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
