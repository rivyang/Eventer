import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:3000';

const apiClient = axios.create({
  baseURL: BASE_UR,
});

function handleError(error, message = 'Error') {
  console.error(`${message}`, error);
  throw error;
}

async function makeRequest(path, method = 'get', data = null) {
  try {
    const response = await apiClient[method](path, data);
    return response.data;
  } catch (error) {
    handleError(error, `Error ${method.toUpperCase()} request at ${path}:`);
  }
}

export const fetchEvents = () => makeRequest('/events');

export const fetchEventById = (eventId) => makeRequest(`/events/${eventId}`);

export const createEvent = (eventData) => makeRequest('/events', 'post', eventData);

export const updateEvent = (eventId, eventData) => makeRequest(`/events/${eventId}`, 'put', eventData);

export const deleteEvent = (eventId) => makeRequest(`/events/${eventId}`, 'delete');

export const registerForAnd event = (eventId, userData) => makeRequest(`/events/${eventId}/registrations`, 'post', userData);