# 🏨 Hotel AI Guest Assistant

A full-stack AI-powered hotel guest assistant that helps hotel guests get information about hotel facilities, policies, rooms, and room availability through a conversational chat interface.

## 🚀 Features

- 💬 Conversational hotel guest assistant
- 🤖 AI/LLM integration path with reliable knowledge-base fallback
- 🏨 Hotel information from a structured JSON knowledge base
- 📅 Room availability checking
- 👥 Guest count validation
- 🔄 Conversation context passed from frontend to backend
- ⚡ Loading and error states in the frontend
- 🛡️ Deterministic availability business logic
- 🔒 API key support through environment variables
- 🧪 Automated backend tests
- 📱 Responsive chat interface
- 🛑 Safe fallback for unsupported questions

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## AI / Knowledge Handling

- Hotel-specific JSON knowledge base
- AI/LLM integration path
- Deterministic fallback responses
- Rule-based intent detection for availability requests

## Data

- JSON-based hotel knowledge base

## Testing

- Pytest
- FastAPI TestClient

---

# 🏗️ Project Architecture

```text
                    ┌──────────────────────┐
                    │      Guest/User      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   React Frontend     │
                    │   Conversational UI  │
                    └──────────┬───────────┘
                               │
                         HTTP / REST API
                               │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend    │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   Chat Route    │          │   Availability   │
       │   /api/chat     │          │ /api/availability│
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   AI Service    │          │   Availability   │
       │                 │          │     Service      │
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌──────────────────┐
       │ Hotel Knowledge │          │ Deterministic    │
       │ Base / Fallback │          │ Business Logic   │
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                └──────────────┬─────────────┘
                               ▼
                    ┌──────────────────────┐
                    │      hotel.json      │
                    │ Hotel / Rooms / FAQs │
                    └──────────────────────┘

                    ## 🤖 AI Approach

The assistant uses a hotel-specific knowledge base stored in `backend/data/hotel.json` to provide reliable answers about hotel facilities, rooms, policies, and FAQs.

The project includes an AI/LLM integration path. The submitted local demo uses deterministic knowledge-base responses as a fallback when an external LLM service is unavailable.

This approach helps:

- Keep hotel information grounded in structured data
- Avoid unsupported hotel claims
- Provide predictable responses
- Keep the application functional without depending completely on an external AI service

---

## 📅 Availability Logic

Room availability is handled using deterministic backend business logic.

The backend function:

```text
checkAvailability(checkIn, checkOut, adults)

performs:

1. Date validation
2. Check-in/check-out validation
3. Past-date validation
4. Guest-count validation
5. Room-capacity matching
6. Available-room response generation


💬 Chat Flow

Guest
  │
  │ "Does the hotel have Wi-Fi?"
  ▼
React Frontend
  │
  │ POST /api/chat
  ▼
FastAPI Backend
  │
  ▼
Hotel Knowledge Base
  │
  ▼
Response
  │
  ▼
React Chat Interface

.
🔌 API Endpoints
Health Check
GET /api/health

Example:

curl http://127.0.0.1:8000/api/health
Chat
POST /api/chat

Example request:

{
  "message": "Does the hotel have Wi-Fi?",
  "conversation": []
}
Room Availability
POST /api/availability

Example request:

{
  "check_in": "2026-09-20",
  "check_out": "2026-09-22",
  "adults": 3
}

Example response:

{
  "check_in": "2026-09-20",
  "check_out": "2026-09-22",
  "adults": 3,
  "available": true,
  "rooms": [
    {
      "name": "Family Room",
      "max_guests": 4,
      "bed": "King Bed + Sofa Bed",
      "price_per_night": 6500,
      "available": true
    },
    {
      "name": "Executive Suite",
      "max_guests": 3,
      "bed": "King Bed + Sofa Bed",
      "price_per_night": 8500,
      "available": true
    }
  ]
}
🧪 Testing

The backend includes automated tests covering:

Health check
Wi-Fi question
Breakfast question
Swimming pool question
Availability intent detection
Room availability
Invalid dates
Missing availability fields
Too many guests
Invalid guest count

Run tests:

python -m pytest -vv

Test result:

10 passed
🛡️ Error Handling

The application handles:

Invalid dates
Check-out before check-in
Invalid guest count
Missing required fields
Unsupported hotel questions
Backend connection failures
External AI service unavailability

For unsupported questions, the assistant provides a safe fallback instead of inventing hotel information.

📱 Frontend UX

The frontend provides:

Conversational chat interface
User and assistant message bubbles
Loading state
Error state
Quick-action buttons
Room availability form
Date validation
Guest selection
Available room cards
Responsive mobile layout

Quick actions:

Wi-Fi
Breakfast
Swimming Pool
Room Availability

🧠 Product & Engineering Decisions

AI vs Deterministic Logic

Natural-language hotel questions can use AI/knowledge-based handling, while business-critical operations such as availability and validation use deterministic backend logic.

Hallucination Prevention

Hotel responses are grounded in the provided hotel knowledge base. When reliable information is unavailable, the assistant uses a fallback response.

Failure Handling

If the backend or external AI service is unavailable, the frontend displays a user-friendly error and the application can fall back to deterministic responses.

🚀 Future Production Improvements


Real hotel/property management system integration
Real-time room inventory
Real booking and payment workflow
Authentication
Persistent conversation storage
Redis/session-based conversation memory
Retrieval-Augmented Generation (RAG)
Production LLM integration
Structured logging and monitoring
Rate limiting
Analytics dashboard
Docker-based deployment
Cloud deployment
Expanded end-to-end testing


🤖 AI Tools Used

ChatGPT — used for architecture planning, implementation assistance, debugging, documentation, and test-case design.
OpenAI API — explored during development as an external LLM integration option. The submitted local demo uses the deterministic hotel knowledge-base fallback when the external service is unavailable.
📂 Project Structure
hotel-ai-guest-assistant/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── data/
│   │   └── hotel.json
│   │
│   ├── tests/
│   │   └── test_api.py
│   │
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── App.css
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
└── README.md
▶️ Running the Project
Backend
cd backend

Activate the virtual environment:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Start the backend:

uvicorn app.main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs
Frontend

Open another terminal:

cd frontend
npm install
npm run dev

Frontend:

http://localhost:5173
👨‍💻 Author

Prajwal HN

B.E. Artificial Intelligence & Machine Learning

GitHub:

https://github.com/Prajwalhn07


