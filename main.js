import axios from 'axios';

const EVENTS_API_URL = process.env.API_URL;

const fetchAllEvents = async () => {
  try {
    const response = await axios.get(`${EVENTS_API_URL}/events`);
    return response.data;
  } catch (error) {
    console.error("Error fetching events:", error);
    return [];
  }
};

const addNewEvent = async (newEventData) => {
  try {
    const response = await axios.post(`${EVENTS_API_URL}/events`, newEventData);
    fetchAllEvents();
    return response.data;
  } catch (error) {
    console.error("Error creating event:", error);
    return null;
  }
};

const signUpForEvent = async (selectedEventId, participantData) => {
  try {
    const response = await axios.post(`${EVENTS_API_URL}/events/${selectedEventId}/register`, participantData);
    alert("Registration successful!");
    return response.data;
  } catch (error) {
    console.error("Error registering for event:", error);
    alert("Failed to register for event.");
    return null;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('fetchEventsBtn').addEventListener('click', fetchAllEvents);
  
  const eventCreationForm = document.getElementById('createEventForm');
  if(eventCreationForm) {
    eventCreationForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(eventCreationForm);
      const newEventData = {
        title: formData.get('title'),
        description: formData.get('description'),
        date: formData.get('date')
      };
      addNewEvent(newEventData);
    });
  }
  
  const eventRegistrationForm = document.getElementById('registerForm');
  if(eventRegistrationForm) {
    eventRegistrationForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(eventRegistrationPerson);
      const selectedEventId = formData.get('eventId');
      const participantData = {
        name: formData.get('name'),
        email: formData.get('email')
      };
      signUpForEvent(selectedEventId, participantData);
    });
  }
});