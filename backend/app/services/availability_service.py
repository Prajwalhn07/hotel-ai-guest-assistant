from datetime import date, datetime
from .hotel_service import load_hotel_data


def validate_dates(check_in: str, check_out: str):
    try:
        check_in_date = datetime.strptime(
            check_in, "%Y-%m-%d"
        ).date()

        check_out_date = datetime.strptime(
            check_out, "%Y-%m-%d"
        ).date()

    except ValueError:
        raise ValueError(
            "Dates must be in YYYY-MM-DD format."
        )

    if check_in_date >= check_out_date:
        raise ValueError(
            "Check-out date must be after check-in date."
        )

    return check_in_date, check_out_date


def check_availability(
    check_in: str,
    check_out: str,
    adults: int
):
    if adults < 1:
        raise ValueError(
            "Number of guests must be at least 1."
        )

    check_in_date, check_out_date = validate_dates(
        check_in,
        check_out
    )

    today = date.today()

    if check_in_date < today:
        raise ValueError(
            "Check-in date cannot be in the past."
        )

    hotel_data = load_hotel_data()

    available_rooms = []

    for room in hotel_data["rooms"]:

        if adults <= room["max_guests"]:

            available_rooms.append({
                "name": room["name"],
                "max_guests": room["max_guests"],
                "bed": room["bed"],
                "price_per_night": room["price_per_night"],
                "available": True
            })

    return {
        "check_in": check_in,
        "check_out": check_out,
        "adults": adults,
        "available": len(available_rooms) > 0,
        "rooms": available_rooms
    }
def is_availability_question(message: str) -> bool:
    keywords = [
        "available",
        "availability",
        "room for",
        "book a room",
        "rooms available",
        "vacancy"
    ]

    message_lower = message.lower()

    return any(
        keyword in message_lower
        for keyword in keywords
    )