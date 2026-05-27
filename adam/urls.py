from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.views import APIView

from .views import SaveViewSet

router = DefaultRouter()
router.register(r"saves", SaveViewSet, basename="save")

# Это оставляем — оно будет отдавать JSON-схему для ReDoc
schema_view = get_schema_view(
    title="Adam API", description="API schema for Adam", version="1.0.0"
)


class RootAPIView(APIView):
    def get(self, request):
        return Response(
            {
                "admin": request.build_absolute_uri("/admin/"),
                "redoc": request.build_absolute_uri("/api/redoc/"),
                "saves": request.build_absolute_uri("/api/saves/"),
            }
        )


urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=False)),
    path("api/", RootAPIView.as_view(), name="api-root"),
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    
    # 1. Переносим сырую схему на отдельный URL
    path("api/schema/", schema_view, name="openapi-schema"),
    
    # 2. А сюда вешаем красивый интерфейс ReDoc, который подгрузит эту схему
    path(
        "api/redoc/",
        TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
