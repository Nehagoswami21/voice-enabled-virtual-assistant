# 🎙️ Voice-Enabled Virtual Assistant Dashboard

> A full-stack voice assistant with real-time speech recognition, text-to-speech responses, WebSocket communication, and a React dashboard — built entirely on free, offline-capable tools.

![Django](https://img.shields.io/badge/Django-4.2-092E20?logo=django) ![React](https://img.shields.io/badge/React-18-61DAFB?logo=react) ![WebSocket](https://img.shields.io/badge/WebSocket-Django_Channels-orange) ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker) ![Vosk](https://img.shields.io/badge/Vosk-Offline_STT-blueviolet)

---

## 💡 What Makes This Special

No paid APIs. No cloud dependency. This assistant runs **fully offline** using Vosk for speech recognition and gTTS for responses. The Django Channels + Redis WebSocket layer gives it real-time feel, and the React dashboard shows live command history and assistant profiles.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎤 Voice Recording | Browser-based audio capture |
| 🧠 Speech Recognition | Vosk offline STT — no API costs |
| 🔊 Text-to-Speech | gTTS responses played back in browser |
| ⚡ Real-time | Django Channels + Redis WebSocket |
| 📊 Dashboard | Command history, logs, assistant profiles |
| 🔐 Auth | Token-based authentication |
| 🐳 Docker Ready | Full containerized stack |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django REST Framework, Django Channels |
| Frontend | React 18, Material UI |
| Speech-to-Text | Vosk (offline, free) |
| Text-to-Speech | gTTS (Google TTS, free) |
| Real-time | Django Channels + Redis |
| Database | SQLite (dev) / PostgreSQL (prod) |
| DevOps | Docker, Docker Compose |

---

## 📁 Project Structure

```
voice-enabled-virtual-assistant/
├── backend/
│   ├── assistant_project/
│   │   ├── settings.py         # Django config + Channels setup
│   │   ├── urls.py
│   │   └── asgi.py             # ASGI for WebSocket support
│   ├── voice_app/
│   │   ├── consumers.py        # WebSocket consumer
│   │   ├── voice_processor.py  # Vosk STT + command engine
│   │   ├── views.py            # REST API views
│   │   ├── models.py           # Command logs, profiles
│   │   └── serializers.py
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── components/
│       │   ├── VoiceRecorder.js    # Audio capture + WebSocket
│       │   ├── Dashboard.js        # Command history UI
│       │   └── Login.js
│       └── services/api.js
├── docker-compose.yml
└── .env.example
```

---

## ⚙️ Setup

### Option 1 — Docker (Recommended)
```bash
git clone https://github.com/Nehagoswami21/voice-enabled-virtual-assistant.git
cd voice-enabled-virtual-assistant
docker-compose up --build
```

Then in a second terminal:
```bash
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
```

### Option 2 — Manual

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000/api/ |
| Django Admin | http://localhost:8000/admin/ |

---

## 📡 API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/token/` | Get auth token |
| GET | `/api/commands/` | List voice commands |
| POST | `/api/commands/process_audio/` | Process audio file |
| GET | `/api/profile/` | Get assistant profile |
| GET | `/api/logs/` | Command history |
| WS | `ws://localhost:8000/ws/voice/` | Real-time voice stream |

---

## 🗣️ Supported Voice Commands

| Command | Response |
|---------|----------|
| "What time is it?" | Current time |
| "Hello" | Greeting response |
| "Help" | Lists available commands |
| "What's the date?" | Current date |

> Extend commands in `voice_app/voice_processor.py`

---

## 💰 Why It's Free

| Component | Alternative | Cost |
|-----------|-------------|------|
| Vosk STT | Google Speech API | $0 vs $0.006/15sec |
| gTTS | Amazon Polly | $0 vs $4/1M chars |
| SQLite | Managed DB | $0 vs $15+/mo |

---

## 📄 License

MIT
