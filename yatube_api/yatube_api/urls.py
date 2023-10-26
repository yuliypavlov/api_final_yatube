from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.views import FollowViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/follow/', FollowViewSet),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
