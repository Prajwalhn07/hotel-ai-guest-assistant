from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.availability import router as availability_router
from app.routes.chat import router as chat_router


app = FastAPI(
    title="Hotel AI Guest Assistant",
    description="Backend API for an AI-powered hotel guest assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(availability_router)
app.include_router(chat_router)


@app.get("/api/health")
def health_check():

    return {
        "status": "ok",
        "service": "hotel-ai-guest-assistant"
    }