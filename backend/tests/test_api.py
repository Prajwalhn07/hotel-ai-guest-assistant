from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_wifi_question():
    response = client.post(
        "/api/chat",
        json={
            "message": "Does the hotel have Wi-Fi?",
            "conversation": []
        }
    )

    assert response.status_code == 200
    assert "Wi-Fi" in response.json()["response"]


def test_breakfast_question():
    response = client.post(
        "/api/chat",
        json={
            "message": "Is breakfast included?",
            "conversation": []
        }
    )

    assert response.status_code == 200
    assert "breakfast" in response.json()["response"].lower()


def test_swimming_pool_question():
    response = client.post(
        "/api/chat",
        json={
            "message": "Does the hotel have a swimming pool?",
            "conversation": []
        }
    )

    assert response.status_code == 200
    assert "swimming pool" in response.json()["response"].lower()


def test_availability_intent():
    response = client.post(
        "/api/chat",
        json={
            "message": "Do you have a room available?",
            "conversation": []
        }
    )

    assert response.status_code == 200
    assert response.json()["intent"] == "availability"


def test_room_availability():
    response = client.post(
        "/api/availability",
        json={
            "check_in": "2026-09-20",
            "check_out": "2026-09-22",
            "adults": 3
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["available"] is True
    assert len(data["rooms"]) == 2


def test_invalid_dates():
    response = client.post(
        "/api/availability",
        json={
            "check_in": "2026-09-22",
            "check_out": "2026-09-20",
            "adults": 3
        }
    )

    assert response.status_code == 400
    assert "Check-out date must be after check-in date" in response.json()["detail"]


def test_missing_availability_fields():
    response = client.post(
        "/api/availability",
        json={
            "check_in": "2026-09-20"
        }
    )

    assert response.status_code == 422


def test_too_many_guests():
    response = client.post(
        "/api/availability",
        json={
            "check_in": "2026-09-20",
            "check_out": "2026-09-22",
            "adults": 6
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["available"] is False
    assert len(data["rooms"]) == 0


def test_invalid_guest_count():
    response = client.post(
        "/api/availability",
        json={
            "check_in": "2026-09-20",
            "check_out": "2026-09-22",
            "adults": 0
        }
    )

    assert response.status_code == 422