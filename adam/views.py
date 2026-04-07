from rest_framework import viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from .models import Save
from .serializers import SaveSerializer


class SaveViewSet(viewsets.ModelViewSet):
    queryset = Save.objects.all()
    serializer_class = SaveSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def perform_destroy(self, instance):
        if instance.save_file:
            instance.save_file.delete(save=False)

        instance.delete()
