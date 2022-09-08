from .models import Mailme
from rest_framework import serializers

class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailme
        fields = '__all__'