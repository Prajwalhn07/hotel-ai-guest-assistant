from fastapi import APIRouter

from app.models.schemas import ChatRequest, ChatResponse
from app.services.ai_service import generate_ai_response
from app.services.availability_service import is_availability_question


router = APIRouter(
    prefix="/api/chat",
    tags=["Chat"]
)


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    availability_intent = is_availability_question(
        request.message
    )

    if availability_intent:
        return ChatResponse(
            response=(
                "I can help you check room availability. "
                "Please provide your check-in date, "
                "check-out date, and number of adults."
            ),
            intent="availability",
            availability=None
        )

    response = generate_ai_response(
        request.message,
        [
            message.model_dump()
            for message in request.conversation
        ]
    )

    return ChatResponse(
        response=response,
        intent="hotel_question",
        availability=None
    )