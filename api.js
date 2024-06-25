import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:3000';

const apiClient = axios.create({
  baseURL: BASE_URL,
});

function handleError(error, message = 'Error') {
    console.error(message, error);
    throw error;
}

export async function fetchEvents() {
    try {
        const response = await apiClient.get('/events');
        return response.data;
    } catch (error) {
        handleError(error, 'Error fetching events:');
    }
}

export async function fetchEventById(eventId) {
    try {
        const response = await apiClient.get(`/events/${eventId}`);
        return response.data;
    } catch (error) {
        handleError(error, `Error fetching event with ID ${eventId}:`);
    }
}

export async function createEvent(eventData) {
    try {
        const response = await apiClient.post('/events', eventData);
        return response.data;
    } catch (error) {
        handleError(error, 'Error creating an event:');
    }
}

export async function updateEvent(eventId, eventData) {
    try {
        const response = await apiClient.put(`/events/${eventId}`, eventData);
        return response.data;
    } catch (error) {
        handleError(error, `Error updating event with ID ${eventId}:`);
    }
}

export async function deleteEvent(eventId) {
    try {
        await apiClient.delete(`/events/${eventId}`);
    } catch (error) {
        handleError(error, `Error deleting event with ID ${eventId}:`);
    }
}

export async function registerForEvent(eventId, userData) {
    try {
        const response = await apiClient.post(`/events/${eventId}/registrations`, userData);
        return response.data;
    } catch (error) {
        handleError(error, `Error registering for event with ID ${eventId}:`);
    }
}