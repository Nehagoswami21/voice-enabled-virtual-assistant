#!/bin/bash

echo "🚀 Setting up Voice Assistant Dashboard..."

# Build and start services
echo "📦 Building Docker containers..."
docker-compose up -d --build

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Run Django migrations
echo "🗄️ Setting up database..."
docker-compose exec -T backend python manage.py migrate

# Create superuser (interactive)
echo "👤 Create admin user:"
docker-compose exec backend python manage.py createsuperuser

echo "✅ Setup complete!"
echo ""
echo "🌐 Access your application:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000/api/"
echo "   Admin: http://localhost:8000/admin/"
echo ""
echo "🎤 Ready to use your voice assistant!"