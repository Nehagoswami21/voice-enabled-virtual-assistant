from django.db import models
from django.contrib.auth.models import User

class VoiceCommand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/', null=True, blank=True)
    transcribed_text = models.TextField()
    response_text = models.TextField()
    audio_response = models.FileField(upload_to='responses/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

class AssistantProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Assistant')
    voice_speed = models.FloatField(default=1.0)
    language = models.CharField(max_length=10, default='en')
    response_style = models.CharField(max_length=50, default='friendly')
    
class CommandLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    command = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)