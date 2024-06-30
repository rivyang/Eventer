class RegistrationForm extends React.Component {
    state = {
        name: '',
        email: '',
        errors: { name: '', email: '' },
    };

    validateForm = () => {
        const { name, email } = this.state;
        let errors = {};
        let formIsValid = true;

        if (!name.trim()) {
            errors.name = 'Name cannot be empty';
            formIsValid = false;
        }

        if (!email.trim()) {
            errors.email = 'Email cannot be empty';
            formIsValid = false;
        } else if (!/\S+@\S+\.\S+/.test(email)) {
            errors.email = 'Email format is invalid';
            formIsValid = false;
        }

        this.setState({ errors });
        return formIsValid;
    }

    handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    handleSubmit = (e) => {
        e.preventDefault();
        if (this.validateForm()) {
            this.props.onRegister(this.state);
        }
    }

    render() {
        const { errors } = this.state;

        return (
            <form onSubmit={this.handleSubmit}>
                <label htmlFor="name">Name:</label>
                <input type="text" id="name" name="name" value={this.state.name} onChange={this.handleChange} />
                <span className="error">{errors.name}</span>

                <label htmlFor="email">Email:</label>
                <input type="email" id="email" name="email" value={this.state.email} onChange={this.handleChange} />
                <span className="error">{errors.email}</span>

                <button type="submit">Register</button>
            </form>
        );
    }
}

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true };
    }

    componentDidCatch(error, errorResources) {
        console.error("Uncaught error:", error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return <h2>Something went wrong.</h2>;
        }

        return this.props.children;
    }
}

const AppWithBoundary = () => (
    <ErrorBoundary>
        <App />
    </ErrorBoundary>
);