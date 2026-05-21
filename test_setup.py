#!/usr/bin/env python3
"""
Simple test script to verify the voice assistant setup
"""

import requests
import json
import time

def test_backend():
    """Test if backend is running"""
    try:
        response = requests.get('http://localhost:8000/api/')
        print("✅ Backend is running")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Backend is not running")
        return False

def test_frontend():
    """Test if frontend is running"""
    try:
        response = requests.get('http://localhost:3000')
        print("✅ Frontend is running")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Frontend is not running")
        return False

def main():
    print("🧪 Testing Voice Assistant Dashboard Setup...")
    print("-" * 50)
    
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    
    print("-" * 50)
    
    if backend_ok and frontend_ok:
        print("🎉 All services are running correctly!")
        print("\n📝 Next steps:")
        print("1. Open http://localhost:3000 in your browser")
        print("2. Login with your admin credentials")
        print("3. Click 'Start Recording' and test voice commands")
    else:
        print("⚠️  Some services are not running. Please check Docker containers:")
        print("   docker-compose ps")

if __name__ == "__main__":
    main()