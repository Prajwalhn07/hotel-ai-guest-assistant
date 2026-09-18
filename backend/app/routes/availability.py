from fastapi import APIRouter, HTTPException

from app.models.schemas import (
    AvailabilityRequest,
    AvailabilityResponse
)

from app.services.availability_service import (
    check_availability
)


router = APIRouter(
    prefix="/api/availability",
    tags=["Availability"]
)


@router.post(
    "",
    response_model=AvailabilityResponse
)
def availability(request: AvailabilityRequest):

    try:

        result = check_availability(
            request.check_in,
            request.check_out,
            request.adults
        )

        return result

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )