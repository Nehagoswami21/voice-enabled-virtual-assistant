from rest_framework import serializers
from .models import VoiceCommand, AssistantProfile, CommandLog

class VoiceCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCommand
        fields = '__all__'
        read_only_fields = ('user',)

class AssistantProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistantProfile
        fields = '__all__'
        read_only_fields = ('user',)

class CommandLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommandLog
        fields = '__all__'
        read_only_fields = ('user',)