import axios from 'axios';

const EVENTS_API_BASE_URL = process.env.API_URL;

const retrieveAllEvents = async () => {
  try {
    const response = await axios.get(`${EVENTS_API_BASE_URL}/events`);
    return response.data;
  } catch (error) {
    console.error("Error retrieving events:", error);
    return [];
  }
};

const createEvent = async (eventDetails) => {
  try {
    const response = await axios.post(`${EVENTS_API_BASE_URL}/events`, eventDetails);
    retrieveAllEvents(); // Refresh the list of events after a new event is added
    return response.data;
  } catch (error) {
    console.error("Error creating a new event:", error);
    return null;
  }
};

const registerForEvent = async (eventId, attendeeDetails) => {
  try {
    const response = await axios.post(`${EVENTS_API_BASE_URL}/events/${eventId}/register`, attendeeDetails);
    alert("Registration successful!");
    return response.data;
  } catch (error) {
    console.error("Error registering for the event:", error);
    alert("Failed to register for the event.");
    return null;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  const fetchEventsButton = document.getElementById('fetchEventsBtn');
  if(fetchEventsButton) {
    fetchEventsButton.addEventListener('click', retrieveAllEvents);
  }
  
  const eventCreationForm = document.getElementById('createEventForm');
  if(eventCreationForm) {
    eventCreationForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(eventCreationForm);
      const eventDetails = {
        title: formData.get('title'),
        description: formData.get('description'),
        date: formData.get('date')
      };
      createEvent(eventHUDetails);
    });
  }
  
  const registrationForm = document.getElementById('registerForm');
  if(registrationForm) {
    registrationForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const formData = new FormData(registrationForm);
      const eventId = formData.get('eventId');
      const attendeeDetails = {
        name: formData.get('name'),
        email: formData.get('email')
      };
      registerForEvent(eventId, attendeeDetails);
    });
  }
});