import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .voice_processor import VoiceProcessor, AssistantEngine

class VoiceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.processor = VoiceProcessor()
        self.engine = AssistantEngine()
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            
            if data['type'] == 'voice_command':
                # Process voice command
                text = data.get('text', '')
                response = self.engine.process_command(text)
                
                await self.send(text_data=json.dumps({
                    'type': 'voice_response',
                    'response': response
                }))
                
        except Exception as e:
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': str(e)
            }))