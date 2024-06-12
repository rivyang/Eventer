# CommunityEvents

Eventer is a web application designed to help users create, manage, and register for community events. It provides a platform for organizing and participating in events within the community.

## Setup Instructions

1. **Install Python**: Ensure Python is installed from [python.org](https://www.python.org/).
2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   ```sh
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
4. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
5. **Set up environment variables**: Create a `.env` file in `server/`:
   ```env
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///app.db
   ```
6. **Run the Flask application**:
   ```sh
   export FLASK_APP=server/app.py
   flask run
   ```

## Features

- **Event Management**: Create, view, and manage community events.
- **Registration**: Register for events and manage your registrations.
- **User Profiles**: Create and manage user profiles.
