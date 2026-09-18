import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
HOTEL_DATA_PATH = BASE_DIR / "data" / "hotel.json"


def load_hotel_data():
    with open(HOTEL_DATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def get_hotel_data():
    return load_hotel_data()


def get_hotel_summary():
    data = load_hotel_data()

    return {
        "hotel": data["hotel"],
        "rooms": data["rooms"],
        "faqs": data["faqs"]
    }