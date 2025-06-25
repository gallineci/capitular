from rest_framework import serializers
from historia.models import Historia

class HistoriaSerializer(serializers.ModelSerializer):
    genero_display = serializers.SerializerMethodField()
    estilo_display = serializers.SerializerMethodField()
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Historia
        exclude = []

    def get_genero_display(self, obj):
        return obj.get_genero_display()

    def get_estilo_display(self, obj):
        return obj.get_estilo_display()

    def get_status_display(self, obj):
        return obj.get_status_display()
