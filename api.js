import axios from 'axios';
const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:3000';
export async function fetchEvents() {
    try {
        const response = await axios.get(`${BASE_URL}/events`);
        return response.data; 
    } catch (error) {
        console.error('Error fetching events:', error);
        throw error; 
    }
}
export async function fetchEventById(eventId) {
    try {
        const response = await axios.get(`${BASE_URL}/events/${eventId}`);
        return response.data; 
    } catch (error) {
        console.error(`Error fetching event with ID ${eventId}:`, error);
        throw error; 
    }
}
export async function createEvent(eventData) {
    try {
        const response = await axios.post(`${BASE_URL}/events`, eventData);
        return response.data; 
    } catch (error) {
util        console.error('Error creating an event:', error);
        throw error; 
    }
}
export async function updateEvent(eventId, eventData) {
    try {
        const response = await axios.put(`${BASE_URL}/events/${eventId}`, eventData);
        return response.data; 
    } catch (error) {
        console.error(`Error updating event with ID ${eventId}:`, error);
        throw error; 
    }
}
export async function deleteEvent(eventId) {
    try {
        await axios.delete(`${BASE_URL}/events/${eventId}`);
    } catch (error) {
        console.error(`Error deleting event with ID ${eventId}:`, error);
        throw error; 
    }
}
export async function registerForEvent(eventId, userData) {
    try {
        const response = await axios.post(`${BASE_URL}/events/${eventId}/registrations`, userData);
        return response.data; 
    } catch (error) {
        console.error(`Error registering for event with ID ${eventId}:`, error);
        throw error; 
    }
}