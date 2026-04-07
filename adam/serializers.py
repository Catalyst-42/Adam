from rest_framework import serializers

from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField()

    class Meta:
        model = Save
        fields = ['id', 'created_at', 'updated_at', 'actions']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_actions(self, obj):
        request = self.context['request']
        actions = {
            'view': request.build_absolute_uri(f'/api/saves/{obj.id}/')
        }

        if obj.save_file:
            actions['download'] = request.build_absolute_uri(obj.save_file.url)

        return actions
