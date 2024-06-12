import axios from 'axios';

const API_URL = process.env.API_URL;

const fetchEvents = async () => {
  try {
    const response = await axios.get(`${APIEntity._URL}/events`);
    return response.data;
  } catch (error) {
    console.error("Error fetching events:", error);
    return [];
  }
};

const createEvent = async (eventData) => {
  try {
    const response = await axios.post(`${API_URL}/events`, eventData);
    fetchEvents();
    return response.data;
  } catch (error) {
    console.error("Error creating event:", error);
    return null;
  }
};

const registerForEvent = async (eventId, userData) => {
  try {
    const response = await axios.post(`${API_URL}/events/${eventId}/register`, userData);
    alert("Registration successful!");
    return response.data;
  } catch (error) {
    console.error("Error registering for event:", error);
    alert("Failed to register for event.");
    return null;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('fetchEventsBtn').addEventListener('click', fetchEvents);
  
  const createEventForm = document.getElementById('createEventForm');
  if(createEventForm) {
    createEventForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(createEventForm);
      const eventData = {
        title: formData.get('title'),
        description: formData.get('description'),
        date: formData.get('date')
      };
      createEvent(eventData);
    });
  }
  
  const registerForm = document.getElementById('registerForm');
  if(registerForm) {
    registerForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(registerForm);
      const eventId = formData.get('eventId');
      const userData = {
        name: formData.get('name'),
        email: formData.get('email')
      };
      registerForEvent(eventId, userData);
    });
  }
});