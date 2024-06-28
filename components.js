import React, { useState, useEffect } from 'react';

const EventList = ({ events, onRegister }) => {
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredEvents, setFilteredEvents] = useState(events);

    useEffect(() => {
        const results = events.filter(event =>
            event.title.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredEvents(results);
    }, [searchTerm, events]);

    return (
        <div className="event-list">
            <input 
                type="text" 
                placeholder="Filter events by title..." 
                value={searchTerm} 
                onChange={(e) => setSearchTerm(e.target.value)} 
            />
            {filteredEvents.map((event) => (
                <div key={event.id} className="event">
                    <h2>{event.title}</h2>
                    <p>{event.description}</p>
                    <span>{event.date}</span>
                    <button onClick={() => onRegister(event.id)}>Register</button>
                </div>
            ))}
        </div>
    );
};

const EventDetails = ({ event }) => {
    return (
        <div className="event-details">
            <h2>{event.title}</h2>
            <p>{event.description}</p>
            <span>{event.date}</span>
            <span>{event.location}</span>
        </div>
    );
};

class RegistrationForm extends React.Component {
    state = {
        name: '',
        email: '',
    };

    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.onRegister(this.state);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="name">Name:</label>
                <input type="text" id="name" name="name" value={this.state.name} onChange={this.handleChange} />

                <label htmlFor="email">Email:</label>
                <input type="email" id="email" name="email" value={this.state.email} onChange={this.handleChange} />

                <button type="submit">Register</button>
            </form>
        );
    }
}

const UserProfile = ({ user }) => {
    return (
        <div className="user-profile">
            <h2>{user.name}</h2>
            <p>Email: {user.email}</p>
            <p>Registered Events: {user.events.join(', ')}</p>
        </div>
    );
};

const App = () => {
    const [events, setEvents] = useState([
        // Your events data goes here
    ]);
    const [user, setUser] = useState({
        name: "",
        email: "",
        events: []
    });

    const handleRegister = (eventId) => {
        const event = events.find(event => event.id === eventId);
        setUser(prevState => ({
            ...prevState,
            events: [...prevState.events, event.title]
        }));
    };

    return (
        <div>
            <EventList events={events} onRegister={handleRegister} />
            <RegistrationForm onRegister={(userData) => setUser(userData)} />
            <UserProfile user={user} />
        </div>
    );
};

export { EventList, EventDetails, RegistrationForm, UserProfile, App };