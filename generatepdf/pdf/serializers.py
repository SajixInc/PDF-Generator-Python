from rest_framework import serializers
from .models import MyModel



class htmltopdfserializer(serializers.ModelSerializer):
    # htmlfile = serializers.FileField()
    class Meta:
        model  =MyModel
        fields = "__all__"


class pdfdownloader(serializers.Serializer):
    pdf_name = serializers.CharField()
    

    

class PdfGenerationSerializer(serializers.Serializer):
    userId = serializers.IntegerField()
