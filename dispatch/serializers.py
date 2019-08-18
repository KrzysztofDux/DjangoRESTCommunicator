from rest_framework import serializers
from .models import Message, Client


class ClientSerializer(serializers.Serializer):
    identity = serializers.CharField(max_length=Client.IDENTITY_LENGTH, read_only=True)

    class Meta:
        model = Client
        fields = ('identity',)

    def create(self, validated_data):
        return Client.objects.create(**validated_data)


class MessageSerializer(serializers.Serializer):
    author = serializers.PrimaryKeyRelatedField(many=False, queryset=Client.objects.all())
    addressee = serializers.PrimaryKeyRelatedField(many=False, queryset=Client.objects.all())
    content = serializers.CharField(allow_blank=True, max_length=Message.MAX_CONTENT_LENGTH)

    class Meta:
        model = Message
        fields = ('author', 'addressee', 'content', 'created')

    def create(self, validated_data):
        return Message.objects.create(**validated_data)
