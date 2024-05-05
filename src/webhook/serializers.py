from rest_framework import serializers


class PersonaSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    id = serializers.CharField(required=True)


class ImageSerializer(serializers.Serializer):
    thumbnail = serializers.CharField(required=True)
    fullframe = serializers.CharField(required=True)


class WebhookSerializer(serializers.Serializer):
    created_date = serializers.CharField(required=True)
    matched_card = PersonaSerializer()
    last_face_event = ImageSerializer()
