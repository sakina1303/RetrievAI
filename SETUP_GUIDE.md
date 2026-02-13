# RetrievAI - AI-Powered Lost & Found Management System

A full-stack web application that leverages AI to help users report and recover lost items efficiently.

## 🚀 Features

### User Features
- **User Authentication**: Secure registration and login with JWT
- **Report Lost Items**: Submit detailed information about lost belongings
- **Report Found Items**: Help others by reporting items you've found
- **AI-Powered Matching**: Automatic similarity matching between lost and found items
- **Smart Claims System**: Submit claims for matched items
- **Track Claims**: Monitor the status of your claims
- **Dashboard**: View statistics and quick actions

### Admin Features
- **Manage Users**: View all registered users
- **Review Claims**: Approve or reject claim requests
- **System Overview**: Monitor all lost and found items
- **Analytics Dashboard**: View system statistics

### AI Features
- **Text Similarity Matching**: Uses Gemini/OpenAI API for intelligent text comparison
- **Smart Suggestions**: Provides confidence scores for matches
- **Automatic Matching**: Runs when new items are reported

---

## 🏗️ System Architecture

### Backend (Flask)
```
backend/
├── app.py                      # Application entry point
├── config.py                   # Configuration settings
├── database.py                 # Database initialization
├── requirements.txt            # Python dependencies
├── models/
│   └── __init__.py            # Database models (User, LostItem, FoundItem, Claim)
├── repositories/
│   ├── user_repository.py     # User data access
│   ├── item_repository.py     # Item data access
│   └── claim_repository.py    # Claim data access
├── services/
│   ├── auth_service.py        # Authentication logic
│   ├── item_service.py        # Item management logic
│   ├── claim_service.py       # Claim management logic
│   └── ai_match_service.py    # AI matching service
├── routes/
│   ├── auth_routes.py         # Authentication endpoints
│   ├── item_routes.py         # Item endpoints
│   ├── claim_routes.py        # Claim endpoints
│   └── admin_routes.py        # Admin endpoints
└── utils/
    ├── file_utils.py          # File upload utilities
    └── decorators.py          # Custom decorators
```

### Frontend (React)
```
frontend/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── main.jsx               # Application entry
    ├── App.jsx                # Main app component
    ├── index.css              # Global styles
    ├── context/
    │   └── AuthContext.jsx    # Authentication context
    ├── utils/
    │   └── api.js             # API client
    ├── components/
    │   ├── Layout.jsx         # Main layout
    │   ├── PrivateRoute.jsx   # Protected routes
    │   └── AdminRoute.jsx     # Admin-only routes
    └── pages/
        ├── Login.jsx          # Login page
        ├── Register.jsx       # Registration page
        ├── Dashboard.jsx      # User dashboard
        ├── ReportLostItem.jsx # Report lost item
        ├── ReportFoundItem.jsx# Report found item
        ├── LostItems.jsx      # View lost items
        ├── FoundItems.jsx     # View found items
        ├── MyClaims.jsx       # User claims
        └── AdminDashboard.jsx # Admin panel
```

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: PostgreSQL (configurable to MySQL)
- **Authentication**: JWT (Flask-JWT-Extended)
- **AI Integration**: Google Gemini API / OpenAI API
- **ORM**: SQLAlchemy
- **File Upload**: Werkzeug

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **UI Library**: Material-UI (MUI)
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Notifications**: React Toastify

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL (or MySQL)
- Gemini API Key or OpenAI API Key

### Backend Setup

1. **Navigate to backend directory**
```bash
cd backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create PostgreSQL database**
```bash
createdb lost_and_found_db
```

5. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your settings:
# - Database URL
# - Secret keys
# - AI API keys (Gemini or OpenAI)
```

6. **Run the application**
```bash
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Create environment file**
```bash
cp .env.example .env
# Edit .env if needed
```

4. **Run development server**
```bash
npm run dev
```

Frontend will run on `http://localhost:3000`

---

## 🔑 Environment Variables

### Backend (.env)
```env
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-key-here
DATABASE_URL=postgresql://username:password@localhost:5432/lost_and_found_db
AI_PROVIDER=gemini
GEMINI_API_KEY=your-gemini-api-key-here
```

### Frontend (.env)
```env
VITE_API_BASE_URL=http://localhost:5000/api
```

---

## 📚 API Documentation

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Items
- `POST /api/items/lost` - Report lost item
- `POST /api/items/found` - Report found item
- `GET /api/items/lost` - Get all lost items
- `GET /api/items/found` - Get all found items
- `GET /api/items/my-lost-items` - Get user's lost items
- `GET /api/items/my-found-items` - Get user's found items
- `GET /api/items/lost/:id/matches` - Get AI matches for lost item
- `GET /api/items/found/:id/matches` - Get AI matches for found item
- `DELETE /api/items/lost/:id` - Delete lost item
- `DELETE /api/items/found/:id` - Delete found item

### Claims
- `POST /api/claims/` - Create claim
- `GET /api/claims/my-claims` - Get user's claims
- `GET /api/claims/:id` - Get claim by ID

### Admin
- `GET /api/admin/users` - Get all users
- `GET /api/admin/claims` - Get all claims
- `GET /api/admin/claims/pending` - Get pending claims
- `POST /api/admin/claims/:id/approve` - Approve claim
- `POST /api/admin/claims/:id/reject` - Reject claim
- `GET /api/admin/items/lost` - Get all lost items
- `GET /api/admin/items/found` - Get all found items

---

## 🎯 Usage Guide

1. **Register/Login**: Create an account or login
2. **Report Lost Item**: Go to "Report Lost" and fill in details
3. **AI Matching**: System automatically finds potential matches
4. **View Matches**: Click "Find Matches" on your lost items
5. **Submit Claim**: Claim a matched found item
6. **Admin Approval**: Admin reviews and approves/rejects claims
7. **Track Status**: Monitor your claims in "My Claims"

---

## 🔐 Security Features

- Password hashing with Werkzeug
- JWT-based authentication
- Protected API routes
- Role-based access control (User/Admin)
- Secure file uploads
- CORS protection

---

## 🎨 Design Patterns

- **Repository Pattern**: Separates data access logic
- **Service Layer Pattern**: Contains business logic
- **MVC Architecture**: Clean separation of concerns
- **Dependency Injection**: Loose coupling between components
- **Factory Pattern**: Used in configuration management

---

## 🧪 Testing

Run backend tests:
```bash
cd backend
python -m pytest
```

Run frontend tests:
```bash
cd frontend
npm test
```

---

## 🚢 Deployment

### Backend Deployment (Example: Heroku)
```bash
heroku create retrievai-backend
heroku addons:create heroku-postgresql:hobby-dev
git push heroku main
```

### Frontend Deployment (Example: Vercel)
```bash
npm run build
vercel --prod
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

- Your Name - Initial work

---

## 🙏 Acknowledgments

- OpenAI/Google for AI APIs
- Material-UI team for the UI components
- Flask and React communities

---

## 📞 Support

For support, email support@retrievai.com or open an issue in the repository.

---

## 🔮 Future Enhancements

- [ ] Image similarity matching using computer vision
- [ ] Email notifications for matches and claims
- [ ] Mobile application (React Native)
- [ ] Real-time chat between users
- [ ] Multi-language support
- [ ] Advanced search and filters
- [ ] Location-based matching
- [ ] QR code generation for items

---

**Built with ❤️ using Flask, React, and AI**
