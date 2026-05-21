from django.contrib import admin
from .models import VoiceCommand, AssistantProfile, CommandLog

@admin.register(VoiceCommand)
class VoiceCommandAdmin(admin.ModelAdmin):
    list_display = ['user', 'transcribed_text', 'created_at']
    list_filter = ['created_at']

@admin.register(AssistantProfile)
class AssistantProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'language']

@admin.register(CommandLog)
class CommandLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'command', 'status', 'timestamp']