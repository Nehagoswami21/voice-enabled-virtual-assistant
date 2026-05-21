from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r'commands', views.VoiceCommandViewSet, basename='voicecommand')
router.register(r'profile', views.AssistantProfileViewSet, basename='assistantprofile')
router.register(r'logs', views.CommandLogViewSet, basename='commandlog')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
]