
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blogapp.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/subscribe/', include('subscription.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)