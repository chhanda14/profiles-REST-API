from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serialize a name field for our APIView"""
    name = serializers.CharField(max_length=10)
