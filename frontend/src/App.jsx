import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! Welcome to Grand Horizon Hotel. How can I help you today?"
    }
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  // Availability form
  const [showAvailability, setShowAvailability] = useState(false);
  const [checkIn, setCheckIn] = useState("");
  const [checkOut, setCheckOut] = useState("");
  const [adults, setAdults] = useState(1);
  const [availabilityLoading, setAvailabilityLoading] = useState(false);
  const [availabilityResult, setAvailabilityResult] = useState(null);
  const [availabilityError, setAvailabilityError] = useState("");

  // Send normal hotel question
  const sendMessage = async () => {
    if (!input.trim() || loading) {
      return;
    }

    const userMessage = {
      role: "user",
      content: input.trim()
    };

    const updatedMessages = [...messages, userMessage];

    setMessages(updatedMessages);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: userMessage.content,
          conversation: messages
        })
      });

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data = await response.json();

      const assistantMessage = {
        role: "assistant",
        content: data.response
      };

      setMessages([...updatedMessages, assistantMessage]);

    } catch (error) {
      setMessages([
        ...updatedMessages,
        {
          role: "assistant",
          content:
            "Sorry, I'm having trouble connecting to the hotel service. Please try again."
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  // Enter key
  const handleKeyDown = (event) => {
    if (event.key === "Enter") {
      sendMessage();
    }
  };

  // Open availability form
  const openAvailability = () => {
    setShowAvailability(true);
    setAvailabilityResult(null);
    setAvailabilityError("");
  };

  // Check room availability
  const checkRoomAvailability = async () => {
    setAvailabilityError("");
    setAvailabilityResult(null);

    if (!checkIn || !checkOut) {
      setAvailabilityError(
        "Please select both check-in and check-out dates."
      );
      return;
    }

    if (checkIn >= checkOut) {
      setAvailabilityError(
        "Check-out date must be after check-in date."
      );
      return;
    }

    if (adults < 1) {
      setAvailabilityError(
        "Number of guests must be at least 1."
      );
      return;
    }

    setAvailabilityLoading(true);

    try {
      const response = await fetch(
        `${API_URL}/api/availability`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            check_in: checkIn,
            check_out: checkOut,
            adults: Number(adults)
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to check availability."
        );
      }

      setAvailabilityResult(data);

    } catch (error) {
      setAvailabilityError(
        error.message ||
          "Unable to check room availability. Please try again."
      );
    } finally {
      setAvailabilityLoading(false);
    }
  };

  const askQuestion = (question) => {
    setInput(question);
    setShowAvailability(false);
  };

  return (
    <div className="app">
      <div className="chat-container">

        {/* Header */}
        <header className="chat-header">
          <div>
            <h1>Grand Horizon Hotel</h1>
            <p>AI Guest Assistant</p>
          </div>

          <div className="status">
            <span></span>
            Online
          </div>
        </header>

        {/* Chat messages */}
        <main className="messages">

          {messages.map((message, index) => (
            <div
              key={index}
              className={`message-row ${message.role}`}
            >
              <div className="message">
                {message.content}
              </div>
            </div>
          ))}

          {loading && (
            <div className="message-row assistant">
              <div className="message typing">
                Thinking...
              </div>
            </div>
          )}

          {/* Availability form */}
          {showAvailability && (
            <div className="availability-panel">

              <h2>Check Room Availability</h2>

              <p className="availability-description">
                Select your dates and number of guests.
              </p>

              <div className="availability-form">

                <div className="form-group">
                  <label>Check-in</label>

                  <input
                    type="date"
                    value={checkIn}
                    onChange={(event) =>
                      setCheckIn(event.target.value)
                    }
                    min={new Date().toISOString().split("T")[0]}
                  />
                </div>

                <div className="form-group">
                  <label>Check-out</label>

                  <input
                    type="date"
                    value={checkOut}
                    onChange={(event) =>
                      setCheckOut(event.target.value)
                    }
                    min={checkIn || new Date().toISOString().split("T")[0]}
                  />
                </div>

                <div className="form-group">
                  <label>Guests</label>

                  <select
                    value={adults}
                    onChange={(event) =>
                      setAdults(Number(event.target.value))
                    }
                  >
                    <option value="1">1 Guest</option>
                    <option value="2">2 Guests</option>
                    <option value="3">3 Guests</option>
                    <option value="4">4 Guests</option>
                    <option value="5">5 Guests</option>
                    <option value="6">6 Guests</option>
                  </select>
                </div>

              </div>

              {availabilityError && (
                <div className="availability-error">
                  {availabilityError}
                </div>
              )}

              <button
                className="availability-button"
                onClick={checkRoomAvailability}
                disabled={availabilityLoading}
              >
                {availabilityLoading
                  ? "Checking..."
                  : "Check Availability"}
              </button>

              {availabilityResult && (
                <div className="availability-results">

                  <h3>
                    {availabilityResult.available
                      ? "Available Rooms"
                      : "No Rooms Available"}
                  </h3>

                  <p className="stay-details">
                    {availabilityResult.check_in} →{" "}
                    {availabilityResult.check_out}
                    {" • "}
                    {availabilityResult.adults} guest
                    {availabilityResult.adults > 1
                      ? "s"
                      : ""}
                  </p>

                  {availabilityResult.rooms.length === 0 ? (
                    <p>
                      No rooms are available for the selected
                      number of guests.
                    </p>
                  ) : (
                    <div className="room-list">

                      {availabilityResult.rooms.map(
                        (room, index) => (
                          <div
                            className="room-card"
                            key={index}
                          >
                            <div className="room-icon">
                              🏨
                            </div>

                            <div className="room-info">
                              <h4>{room.name}</h4>

                              <p>{room.bed}</p>

                              <p>
                                Up to {room.max_guests} guests
                              </p>
                            </div>

                            <div className="room-price">
                              <strong>
                                ₹
                                {room.price_per_night.toLocaleString(
                                  "en-IN"
                                )}
                              </strong>

                              <span>
                                per night
                              </span>
                            </div>
                          </div>
                        )
                      )}

                    </div>
                  )}

                </div>
              )}

            </div>
          )}

        </main>

        {/* Quick actions */}
        <div className="quick-actions">

          <button
            onClick={() =>
              askQuestion("Does the hotel have Wi-Fi?")
            }
          >
            Wi-Fi
          </button>

          <button
            onClick={() =>
              askQuestion("Is breakfast included?")
            }
          >
            Breakfast
          </button>

          <button
            onClick={() =>
              askQuestion(
                "Does the hotel have a swimming pool?"
              )
            }
          >
            Swimming Pool
          </button>

          <button onClick={openAvailability}>
            Room Availability
          </button>

        </div>

        {/* Message input */}
        <footer className="input-area">

          <input
            type="text"
            placeholder="Ask about the hotel..."
            value={input}
            onChange={(event) =>
              setInput(event.target.value)
            }
            onKeyDown={handleKeyDown}
            disabled={loading}
          />

          <button
            onClick={sendMessage}
            disabled={loading}
          >
            {loading ? "..." : "Send"}
          </button>

        </footer>

      </div>
    </div>
  );
}

export default App;