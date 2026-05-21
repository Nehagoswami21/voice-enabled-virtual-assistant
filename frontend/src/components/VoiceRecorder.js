import React, { useState, useRef } from 'react';
import { Button, Box, Typography, CircularProgress } from '@mui/material';
import { Mic, Stop, PlayArrow } from '@mui/icons-material';
import apiService from '../services/api';

const VoiceRecorder = ({ onResponse }) => {
  const [isRecording, setIsRecording] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      chunksRef.current = [];

      mediaRecorderRef.current.ondataavailable = (event) => {
        chunksRef.current.push(event.data);
      };

      mediaRecorderRef.current.onstop = async () => {
        const audioBlob = new Blob(chunksRef.current, { type: 'audio/wav' });
        const audioFile = new File([audioBlob], 'recording.wav', { type: 'audio/wav' });
        
        setIsProcessing(true);
        try {
          const response = await apiService.processAudio(audioFile);
          onResponse(response);
          if (response.audio_response_url) {
            setAudioUrl(response.audio_response_url);
          }
        } catch (error) {
          console.error('Error processing audio:', error);
        }
        setIsProcessing(false);
      };

      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error('Error accessing microphone:', error);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop());
      setIsRecording(false);
    }
  };

  const playResponse = () => {
    if (audioUrl) {
      const audio = new Audio(audioUrl);
      audio.play();
    }
  };

  return (
    <Box sx={{ textAlign: 'center', p: 3 }}>
      <Typography variant="h6" gutterBottom>
        Voice Assistant
      </Typography>
      
      <Box sx={{ mb: 2 }}>
        {!isRecording && !isProcessing && (
          <Button
            variant="contained"
            color="primary"
            size="large"
            startIcon={<Mic />}
            onClick={startRecording}
          >
            Start Recording
          </Button>
        )}
        
        {isRecording && (
          <Button
            variant="contained"
            color="error"
            size="large"
            startIcon={<Stop />}
            onClick={stopRecording}
          >
            Stop Recording
          </Button>
        )}
        
        {isProcessing && (
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <CircularProgress size={24} sx={{ mr: 1 }} />
            <Typography>Processing...</Typography>
          </Box>
        )}
      </Box>
      
      {audioUrl && (
        <Button
          variant="outlined"
          startIcon={<PlayArrow />}
          onClick={playResponse}
          sx={{ mt: 1 }}
        >
          Play Response
        </Button>
      )}
    </Box>
  );
};

export default VoiceRecorder;