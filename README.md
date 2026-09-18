# 🏨 Hotel AI Guest Assistant

A full-stack AI-powered hotel guest assistant that helps hotel guests get information about hotel facilities, policies, rooms, and room availability through a conversational chat interface.

## 🚀 Features

- 💬 Conversational hotel guest assistant
- 🤖 AI-powered responses using OpenAI API
- 🏨 Hotel information from a structured JSON knowledge base
- 📅 Room availability checking
- 👥 Guest count validation
- 🔄 Conversation context support
- ⚡ Loading and error states in the frontend
- 🛡️ Deterministic availability business logic
- 🔒 API key stored securely in environment variables
- 🧪 Automated backend tests
- 📱 Responsive chat interface

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

## AI

- OpenAI API
- GPT-4o-mini

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
                    │     FastAPI Backend  │
                    └──────────┬───────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   Chat Route    │          │ Availability     │
       │   /api/chat     │          │ /api/availability│
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   AI Service    │          │ Availability     │
       │                 │          │ Service          │
       └────────┬────────┘          └────────┬─────────┘
                │                            │
                ▼                            ▼
       ┌─────────────────┐          ┌──────────────────┐
       │   OpenAI API    │          │ Hotel Knowledge  │
       │                 │          │ Base             │
       └─────────────────┘          │ hotel.json       │
                                    └──────────────────┘