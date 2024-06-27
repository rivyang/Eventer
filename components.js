import React from 'react';

const EventList = ({ events }) => {
    return (
        <div className="event-list">
            {events.map((event) => (
                <div key={event.id} className="event">
                    <h2>{event.title}</h2>
                    <p>{event.description}</p>
                    <span>{event.date}</span>
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

export { EventList, EventDetails, RegistrationForm, UserProfile };