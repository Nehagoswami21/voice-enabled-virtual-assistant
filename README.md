# Voice-Enabled Virtual Assistant Dashboard

A complete voice assistant dashboard built with Django REST Framework and React, optimized for free resources.

## Features

- 🎤 Voice recording and processing
- 🗣️ Text-to-speech responses
- 📊 Interactive dashboard
- 📝 Command history and logs
- ⚙️ Configurable assistant profiles
- 🔐 Token-based authentication
- 🔄 Real-time WebSocket communication

## Tech Stack

- **Backend**: Django REST Framework, Vosk (speech recognition), gTTS (text-to-speech)
- **Frontend**: React, Material UI
- **Database**: SQLite (development) / PostgreSQL (production)
- **Real-time**: Django Channels + Redis
- **Containerization**: Docker + Docker Compose

## Quick Start

### Prerequisites
- Docker and Docker Compose
- Microphone access for voice recording

### Setup

1. **Clone and start services**:
```bash
docker-compose up --build
```

2. **Setup Django (in another terminal)**:
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

3. **Access the application**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/

### Usage

1. **Login** with your created superuser credentials
2. **Click "Start Recording"** to record voice commands
3. **Speak naturally** - try commands like:
   - "What time is it?"
   - "Hello"
   - "Help"
4. **View responses** in the dashboard
5. **Check history** in the Recent Commands panel

## API Endpoints

- `POST /api/auth/token/` - Get authentication token
- `GET /api/commands/` - List voice commands
- `POST /api/commands/process_audio/` - Process audio file
- `GET /api/profile/` - Get assistant profile
- `GET /api/logs/` - Get command logs

## Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

### Adding New Commands

Edit `backend/voice_app/voice_processor.py` and add to the `AssistantEngine.commands` dictionary:

```python
def my_command(self, text):
    return "Custom response"

# Add to __init__:
self.commands['keyword'] = self.my_command
```

## Production Deployment

1. **Update settings** for production:
   - Change `SECRET_KEY` in settings.py
   - Set `DEBUG = False`
   - Configure PostgreSQL database
   - Set proper CORS settings

2. **Environment variables**:
```bash
export DATABASE_URL=postgresql://user:pass@localhost/dbname
export DEBUG=False
export SECRET_KEY=your-secret-key
```

## Free Resource Optimization

- **Vosk**: Offline speech recognition (no API costs)
- **gTTS**: Free Google Text-to-Speech
- **SQLite**: No database hosting costs for development
- **Local processing**: No external AI API calls required

## Troubleshooting

### Audio Issues
- Ensure microphone permissions are granted
- Check browser compatibility (Chrome/Firefox recommended)
- Verify audio format support

### Docker Issues
```bash
docker-compose down -v
docker-compose up --build
```

### Database Issues
```bash
docker-compose exec backend python manage.py migrate --run-syncdb
```

## License

MIT License - feel free to use for personal and commercial projects.