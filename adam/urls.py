"""
URL configuration for adam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.views import APIView

from .views import SaveViewSet

router = DefaultRouter()
router.register(r'saves', SaveViewSet, basename='save')

schema_view = get_schema_view(
    title='Adam API',
    description='API schema for Adam',
    version='1.0.0'
)

class RootAPIView(APIView):
    def get(self, request):
        return Response({
            'admin': request.build_absolute_uri('/admin/'),
            'redoc': request.build_absolute_uri('/api/redoc/'),
            'saves': request.build_absolute_uri('/api/saves/'),
        })

urlpatterns = [
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    path('api/', RootAPIView.as_view(), name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/redoc/', schema_view, name='redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
