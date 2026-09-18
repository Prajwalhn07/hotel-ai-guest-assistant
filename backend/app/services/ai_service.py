from app.services.hotel_service import load_hotel_data


def generate_ai_response(message: str, conversation: list):
    data = load_hotel_data()

    hotel = data["hotel"]
    rooms = data["rooms"]

    message_lower = message.lower()

    # Wi-Fi
    if "wifi" in message_lower or "wi-fi" in message_lower:
        return "Yes, complimentary Wi-Fi is available throughout the hotel."

    # Breakfast
    if "breakfast" in message_lower:
        return (
            f"Yes, breakfast is included. "
            f"It is served from {hotel['breakfast']['timing']}."
        )

    # Swimming pool
    if "swimming pool" in message_lower or "pool" in message_lower:
        return "Yes, the hotel has a swimming pool."

    # Check-in
    if "check in" in message_lower or "check-in" in message_lower:
        return f"Check-in time is {hotel['check_in']}."

    # Check-out
    if "check out" in message_lower or "check-out" in message_lower:
        return f"Check-out time is {hotel['check_out']}."

    # Parking
    if "parking" in message_lower:
        return "Yes, parking is available at the hotel."

    # Restaurant
    if "restaurant" in message_lower:
        return "Yes, the hotel has a restaurant."

    # Gym
    if "gym" in message_lower:
        return "Yes, the hotel has a gym."

    # Cancellation policy
    if "cancel" in message_lower or "cancellation" in message_lower:
        return hotel["cancellation_policy"]

    # Hotel amenities
    if "amenities" in message_lower or "facilities" in message_lower:
        return (
            "The hotel offers: "
            + ", ".join(hotel["amenities"])
            + "."
        )

    # Hotel location
    if "location" in message_lower or "where is the hotel" in message_lower:
        return f"The hotel is located in {hotel['location']}."

    # Room information
    if "room" in message_lower:
        room_details = []

        for room in rooms:
            room_details.append(
                f"{room['name']} - up to {room['max_guests']} guests, "
                f"{room['bed']}, "
                f"₹{room['price_per_night']} per night"
            )

        return "Our rooms are: " + "; ".join(room_details) + "."

    # Fallback for unsupported questions
    return (
        "I don't have reliable information about that question. "
        "I can help with rooms, Wi-Fi, breakfast, swimming pool, "
        "gym, parking, restaurant, check-in, check-out, "
        "cancellation policy, hotel amenities, and location."
    )