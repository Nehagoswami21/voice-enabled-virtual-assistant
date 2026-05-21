import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class ApiService {
  constructor() {
    this.api = axios.create({
      baseURL: `${API_BASE_URL}/api/`,
    });
    
    this.api.interceptors.request.use((config) => {
      const token = localStorage.getItem('token');
      if (token) {
        config.headers.Authorization = `Token ${token}`;
      }
      return config;
    });
  }

  async login(username, password) {
    const response = await this.api.post('auth/token/', { username, password });
    localStorage.setItem('token', response.data.token);
    return response.data;
  }

  logout() {
    localStorage.removeItem('token');
  }

  async getCommands() {
    const response = await this.api.get('commands/');
    return response.data;
  }

  async processAudio(audioFile) {
    const formData = new FormData();
    formData.append('audio', audioFile);
    const response = await this.api.post('commands/process_audio/', formData);
    return response.data;
  }

  async getProfile() {
    const response = await this.api.get('profile/');
    return response.data[0] || {};
  }

  async updateProfile(data) {
    const response = await this.api.patch('profile/1/', data);
    return response.data;
  }

  async getLogs() {
    const response = await this.api.get('logs/');
    return response.data;
  }
}

export default new ApiService();