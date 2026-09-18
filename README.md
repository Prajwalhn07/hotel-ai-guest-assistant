# 🏨 Grand Horizon Hotel — AI Guest Assistant

An AI-powered full-stack hotel guest assistant that helps guests get information about hotel facilities, policies, rooms, and availability through a conversational interface.

## 📌 Project Overview

The Grand Horizon Hotel AI Guest Assistant provides a simple chat-based experience for hotel guests.

Guests can:

- Ask questions about hotel facilities
- Ask about breakfast and timings
- Ask about check-in and check-out
- Ask about hotel amenities
- Check room availability
- Provide check-in and check-out dates
- Provide the number of guests
- Receive available room details and prices
- Receive helpful fallback responses when information is unavailable

The application uses deterministic backend logic for business-critical availability decisions and an AI service for natural-language hotel questions.

---

# ✨ Features

## Guest Chat

Guests can ask questions such as:

- Does the hotel have Wi-Fi?
- Is breakfast included?
- Does the hotel have a swimming pool?
- What time is check-in?
- What time is check-out?

## Room Availability

Guests can provide:

- Check-in date
- Check-out date
- Number of guests

The backend checks room capacity and returns matching rooms.

## Error Handling

The application handles:

- Missing availability information
- Invalid dates
- Check-out before check-in
- Invalid guest counts
- Backend connection failures
- AI service failures
- Unsupported hotel questions

## Responsive Interface

The frontend provides a conversational interface designed for both desktop and mobile screens.

---

# 🛠️ Tech Stack

## Frontend

- React
- Vite
- JavaScript
- CSS
- Fetch API

## Backend

- Python
- FastAPI
- Pydantic
- Uvicorn

## AI

- OpenAI API
- AI-powered hotel question answering
- Hotel knowledge context
- Fallback handling

## Data

- JSON-based hotel knowledge base

## Testing

- Pytest
- FastAPI TestClient

---

# 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │       Guest         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React Frontend    │
                    │      + Vite         │
                    └──────────┬──────────┘
                               │
                         HTTP / JSON
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │ Chat Route  │ │ Availability│ │ Hotel Data  │
        │ /api/chat   │ │ /api/       │ │ hotel.json  │
        │             │ │ availability│ │             │
        └──────┬──────┘ └──────┬──────┘ └─────────────┘
               │               │
               ▼               ▼
        ┌─────────────┐ ┌─────────────┐
        │ AI Service  │ │ Availability│
        │             │ │ Service     │
        └──────┬──────┘ └─────────────┘
               │
               ▼
        ┌─────────────┐
        │ OpenAI API  │
        └─────────────┘