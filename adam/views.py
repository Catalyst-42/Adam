from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import json
from .models import Save
from .serializers import SaveSerializer


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    parser_classes = [MultiPartParser]
    http_method_names = ["get", "put", "head", "delete"]

    def get_object(self):
        try:
            return Save.objects.get(pk=self.kwargs.get("pk"))
        except Save.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        file_content = instance.file.read()
        data = json.loads(file_content.decode("utf-8"))
        return Response(data)

    def update(self, request, *args, **kwargs):
        save_id = kwargs.get("pk")
        file_obj = request.FILES.get("file")

        if not file_obj:
            return Response(
                {"error": "file required"}, status=status.HTTP_400_BAD_REQUEST
            )

        file_content = file_obj.read()
        data = json.loads(file_content.decode("utf-8"))
        name = data.get("name", "Сохранение")

        # Delete old file if exists
        existing = Save.objects.filter(id=save_id).first()
        if existing and existing.file:
            existing.file.delete(save=False)

        # Create or update with new file and extracted name
        save, created = Save.objects.update_or_create(
            id=save_id, defaults={"file": file_obj, "name": name}
        )

        return Response(
            {"id": save.id},
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )

    def perform_destroy(self, instance):
        instance.delete()
