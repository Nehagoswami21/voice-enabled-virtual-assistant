import json
import os
import tempfile
import wave
from gtts import gTTS
from io import BytesIO
import vosk

class VoiceProcessor:
    def __init__(self):
        # Download Vosk model if not exists (small English model)
        model_path = "/tmp/vosk-model"
        if not os.path.exists(model_path):
            os.makedirs(model_path, exist_ok=True)
        
        try:
            self.model = vosk.Model(model_path)
        except:
            # Fallback to basic text processing if Vosk model not available
            self.model = None
    
    def speech_to_text(self, audio_file):
        if not self.model:
            return "Speech recognition not available"
        
        try:
            rec = vosk.KaldiRecognizer(self.model, 16000)
            
            with wave.open(audio_file, 'rb') as wf:
                results = []
                while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        break
                    if rec.AcceptWaveform(data):
                        results.append(json.loads(rec.Result())['text'])
                
                final_result = json.loads(rec.FinalResult())
                if final_result['text']:
                    results.append(final_result['text'])
                
                return ' '.join(results)
        except Exception as e:
            return f"Error processing audio: {str(e)}"
    
    def text_to_speech(self, text, language='en'):
        try:
            tts = gTTS(text=text, lang=language, slow=False)
            audio_buffer = BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            return audio_buffer
        except Exception as e:
            return None

class AssistantEngine:
    def __init__(self):
        self.commands = {
            'time': self.get_time,
            'weather': self.get_weather,
            'hello': self.greet,
            'help': self.show_help,
        }
    
    def process_command(self, text):
        text = text.lower().strip()
        
        for command, handler in self.commands.items():
            if command in text:
                return handler(text)
        
        return "I'm not sure how to help with that. Try saying 'help' for available commands."
    
    def get_time(self, text):
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"
    
    def get_weather(self, text):
        return "I can't check the weather right now, but it's a great day to code!"
    
    def greet(self, text):
        return "Hello! I'm your voice assistant. How can I help you today?"
    
    def show_help(self, text):
        return "I can help with: time, weather, greetings. Just speak naturally!"