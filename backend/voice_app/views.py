from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile
from django.http import HttpResponse
from .models import VoiceCommand, AssistantProfile, CommandLog
from .serializers import VoiceCommandSerializer, AssistantProfileSerializer, CommandLogSerializer
from .voice_processor import VoiceProcessor, AssistantEngine

class VoiceCommandViewSet(viewsets.ModelViewSet):
    serializer_class = VoiceCommandSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return VoiceCommand.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def process_audio(self, request):
        audio_file = request.FILES.get('audio')
        if not audio_file:
            return Response({'error': 'No audio file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        processor = VoiceProcessor()
        engine = AssistantEngine()
        
        # Process speech to text
        transcribed_text = processor.speech_to_text(audio_file)
        
        # Generate response
        response_text = engine.process_command(transcribed_text)
        
        # Generate audio response
        audio_response = processor.text_to_speech(response_text)
        
        # Save command
        command = VoiceCommand.objects.create(
            user=request.user,
            audio_file=audio_file,
            transcribed_text=transcribed_text,
            response_text=response_text
        )
        
        if audio_response:
            command.audio_response.save(
                f'response_{command.id}.mp3',
                ContentFile(audio_response.getvalue())
            )
        
        # Log command
        CommandLog.objects.create(
            user=request.user,
            command=transcribed_text[:200],
            status='success'
        )
        
        return Response({
            'id': command.id,
            'transcribed_text': transcribed_text,
            'response_text': response_text,
            'audio_response_url': command.audio_response.url if command.audio_response else None
        })

class AssistantProfileViewSet(viewsets.ModelViewSet):
    serializer_class = AssistantProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        profile, created = AssistantProfile.objects.get_or_create(user=self.request.user)
        return AssistantProfile.objects.filter(user=self.request.user)

class CommandLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommandLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return CommandLog.objects.filter(user=self.request.user)[:50]