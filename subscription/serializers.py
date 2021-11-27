from rest_framework import serializers
from .models import SubscribedMail
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribedMail
        fields = '__all__'
