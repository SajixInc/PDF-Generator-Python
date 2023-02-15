from rest_framework import serializers


class PdfGenerationSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
