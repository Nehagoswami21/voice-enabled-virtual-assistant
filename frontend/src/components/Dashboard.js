import React, { useState, useEffect } from 'react';
import {
  Container,
  Grid,
  Paper,
  Typography,
  List,
  ListItem,
  ListItemText,
  Box,
  Card,
  CardContent
} from '@mui/material';
import VoiceRecorder from './VoiceRecorder';
import apiService from '../services/api';

const Dashboard = () => {
  const [commands, setCommands] = useState([]);
  const [logs, setLogs] = useState([]);
  const [currentResponse, setCurrentResponse] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const [commandsData, logsData] = await Promise.all([
        apiService.getCommands(),
        apiService.getLogs()
      ]);
      setCommands(commandsData.slice(0, 10));
      setLogs(logsData.slice(0, 10));
    } catch (error) {
      console.error('Error loading data:', error);
    }
  };

  const handleVoiceResponse = (response) => {
    setCurrentResponse(response);
    loadData(); // Refresh data
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Voice Assistant Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <VoiceRecorder onResponse={handleVoiceResponse} />
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Current Response
            </Typography>
            {currentResponse ? (
              <Card>
                <CardContent>
                  <Typography variant="subtitle2" color="textSecondary">
                    You said:
                  </Typography>
                  <Typography variant="body1" gutterBottom>
                    {currentResponse.transcribed_text}
                  </Typography>
                  <Typography variant="subtitle2" color="textSecondary">
                    Assistant response:
                  </Typography>
                  <Typography variant="body1">
                    {currentResponse.response_text}
                  </Typography>
                </CardContent>
              </Card>
            ) : (
              <Typography color="textSecondary">
                No recent interactions
              </Typography>
            )}
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Recent Commands
            </Typography>
            <List>
              {commands.map((command) => (
                <ListItem key={command.id}>
                  <ListItemText
                    primary={command.transcribed_text}
                    secondary={new Date(command.created_at).toLocaleString()}
                  />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Grid>
        
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Activity Log
            </Typography>
            <List>
              {logs.map((log) => (
                <ListItem key={log.id}>
                  <ListItemText
                    primary={log.command}
                    secondary={`${log.status} - ${new Date(log.timestamp).toLocaleString()}`}
                  />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;