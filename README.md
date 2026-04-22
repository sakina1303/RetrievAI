# RetrievAI - AI-Powered Lost & Found Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg)](https://reactjs.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-000000.svg)](https://flask.palletsprojects.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-336791.svg)](https://www.postgresql.org/)

An intelligent full-stack Lost & Found platform that helps users report lost and found items and uses AI-based similarity matching to suggest possible matches automatically.

This system improves the efficiency of recovering lost items and demonstrates strong backend architecture, OOP principles, and system design.

---

## Problem Statement

Losing personal belongings in public places like colleges, offices, airports, and malls is common. Traditional lost and found systems are manual and inefficient.

This system provides a centralized platform with AI-powered matching to help users recover items faster.

---

## Hosted url
https://www.unboundxinc.com/

## Key Features

### User Features
- User Registration and Login (JWT Authentication)
- Report Lost Items with description, image, and location
- Report Found Items to help others
- AI-powered matching suggestions with confidence scores
- Submit claim requests for matched items
- View claim status and history
- Personal dashboard with statistics

### Admin Features
- View all users
- View all lost and found items
- Approve or reject claim requests
- System analytics and management

### AI Features
- Text similarity matching using Gemini/OpenAI API
- Confidence scoring for matches
- Automatic match suggestions
- Fallback to basic matching if API unavailable

---

## System Architecture

The backend follows **clean architecture principles**:

```
Controllers → handle HTTP requests  
Services → contain business logic  
Repositories → handle database operations  
Models → represent entities  
AI Service → handles matching logic  
```

This ensures **scalability, modularity, and maintainability**.

---

## Tech Stack

### Frontend
- React.js 18
- Material-UI (MUI)
- React Router v6
- Axios
- Vite

### Backend
- Flask (Python)
- SQLAlchemy ORM
- Flask-JWT-Extended
- PostgreSQL
- REST APIs

### AI Integration
- Google Gemini API
- OpenAI API

---

## Implemented Modules

### Backend
- Flask app bootstrap and configuration
- SQLAlchemy models for users, lost items, found items, and claims
- Repository layer for database access
- Service layer for authentication, item handling, claims, and AI matching
- JWT-protected REST routes for auth, items, claims, and admin workflows
- File upload handling and admin access control

### Frontend
- React app with Vite and Material UI
- Authentication flow with login, registration, and token persistence
- Protected dashboard, lost item, found item, claims, and admin pages
- AI match browsing and claim submission UI
- API client with backend proxy integration

---

## Project Structure

```
RetrievAI/
├── README.md
├── SETUP_GUIDE.md          # Detailed setup instructions
├── QUICKSTART.md           # Quick start guide
├── API_TESTING.md          # API testing guide
├── idea.md                 # Project concept
├── useCaseDiagram.md       # Use case diagrams
├── sequenceDiagram.md      # Sequence diagrams
├── classDiagram.md         # Class diagrams
├── ErDiagram.md            # ER diagrams
├── backend/                # Flask backend
│   ├── app.py
│   ├── config.py
│   ├── database.py
│   ├── requirements.txt
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── routes/
│   └── utils/
└── frontend/               # React frontend
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── context/
        ├── utils/
        ├── components/
        └── pages/
```

---

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- Gemini API Key or OpenAI API Key

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python app.py
```

Backend runs on `http://localhost:5001`

The backend uses a local SQLite database by default, so the app can run without a separate database server during development. Set `DATABASE_URL` in `backend/.env` if you want PostgreSQL or MySQL.

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

**📖 For detailed setup instructions, see [SETUP_GUIDE.md](SETUP_GUIDE.md)**

---

## Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Get started in 5 minutes
- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Complete installation and configuration guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deploy to Render (production)
- **[RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)** - Quick Render deployment (3 steps)
- **[API_TESTING.md](API_TESTING.md)** - API testing with cURL and Postman
- **[idea.md](idea.md)** - Original project concept
- **Diagrams** - See useCaseDiagram.md, sequenceDiagram.md, classDiagram.md, ErDiagram.md

---

## Core Entities

- **User** - System users (regular and admin)
- **LostItem** - Items reported as lost
- **FoundItem** - Items reported as found
- **Claim** - Claim requests for matched items
- **AIMatchService** - AI-powered matching engine

---

## Authentication

The system uses **JWT (JSON Web Tokens)** for secure authentication:
- Passwords are hashed using Werkzeug
- Tokens expire after 24 hours
- Role-based access control (User/Admin)

---

## AI Matching

The AI matching service:
1. Compares text descriptions of lost and found items
2. Uses Gemini or OpenAI API for semantic similarity
3. Returns confidence scores (0-1 scale)
4. Provides match confidence labels (Low, Medium, High, Very High)
5. Falls back to basic word overlap if API unavailable

### Where AI Scan Happens in UI
- Lost item flow: `My Lost Items` -> click `Find Matches` on a specific lost item.
- Found item flow: `My Found Items` -> click `Find Matches` on a specific found item.
- Each click calls the backend AI match endpoints and shows scored suggestions in a dialog.

### Claim Flow in UI
1. Report a lost item.
2. Open `My Lost Items` and run `Find Matches`.
3. Click `Claim` on a matching found item.
4. Track status (`pending`, `approved`, `rejected`) in `My Claims`.
5. Admin reviews pending claims in `Admin Dashboard`.

---

## Screenshots

*Coming soon - Add screenshots of your application here*

---

## Testing

Test the system by:
1. Registering a user account
2. Reporting a lost item (e.g., "Blue iPhone")
3. Reporting a found item with similar description
4. Clicking "Find Matches" to see AI suggestions
5. Submitting a claim
6. Login as admin to approve claims

---

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Authors

- Initial development for educational purposes

---

## Acknowledgments

- Google Gemini / OpenAI for AI APIs
- Flask and React communities
- Material-UI for excellent components

---

## Support

For issues and questions:
- Open an issue on GitHub
- Check documentation files

---

## Future Enhancements

- [ ] Image similarity using computer vision
- [ ] Email notifications
- [ ] Mobile app (React Native)
- [ ] Real-time chat
- [ ] Multi-language support
- [ ] Advanced search filters
- [ ] QR code generation

---

**Built with ❤️ using Flask, React, and AI**

## How Matching Works

1. User reports lost item
2. System stores item in database
3. AI compares lost item with found items
4. System returns possible matches
5. User submits claim request
6. Admin approves or rejects claim
7. Item status updated and moved to history

---

## Backend Design Principles Used

- Object-Oriented Programming (OOP)
- Encapsulation
- Abstraction
- Service Layer Architecture
- Separation of Concerns
- Clean Code Structure

---

## Future Enhancements

- Image-based matching using AI Vision models
- Email notifications
- Real-time alerts
- Mobile application support

---

## Author

Sakina  
Full Stack Developer | AI Enthusiast

---

## Status

Milestone-1 Completed  
Idea and system design ready  
Implementation in progress
