class RegistrationForm extends React.Component {
    state = {
        userName: '',
        userEmail: '',
        validationErrors: { userName: '', userEmail: '' },
    };

    isFormValid = () => {
        const { userName, userEmail } = this.state;
        let validationErrors = {};
        let isFormValid = true;

        if (!userName.trim()) {
            validationErrors.userName = 'Name cannot be empty';
            isFormValid = false;
        }

        if (!userEmail.trim()) {
            validationErrors.userEmail = 'Email cannot be empty';
            isFormValid = false;
        } else if (!/\S+@\S+\.\S+/.test(userEmail)) {
            validationErrors.userEmail = 'Email format is invalid';
            isFormValid = false;
        }

        this.setState({ validationErrors });
        return isFormValid;
    }

    handleInputChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    handleFormSubmit = (e) => {
        e.preventDefault();
        if (this.isFormValid()) {
            this.props.onUserRegister(this.state);
        }
    }

    render() {
        const { validationErrors, userName, userEmail } = this.state;

        return (
            <form onSubmit={this.handleFormSubmit}>
                <label htmlFor="userName">Name:</label>
                <input type="text" id="userName" name="userName" value={userName} onChange={this.handleInputChange} />
                <span className="error">{validationErrors.userName}</span>

                <label htmlFor="userEmail">Email:</label>
                <input type="email" id="userEmail" name="userEmail" value={userEmail} onChange={this.handleInputChange} />
                <span className="error">{validationErrors.userEmail}</span>

                <button type="submit">Register</button>
            </form>
        );
    }
}

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasErrorOccurred: false };
    }

    static getDerivedStateFromError(error) {
        return { hasErrorOccurred: true };
    }

    logErrorToConsole = (error, errorInfo) => {
        console.error("Uncaught error:", error, errorInfo);
    }

    componentDidCatch(error, errorExpert) {
        this.logErrorToConsole(error, errorExpert);
    }

    render() {
        if (this.state.hasErrorOccurred) {
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