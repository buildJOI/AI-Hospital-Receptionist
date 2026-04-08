import { useState } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [patientData, setPatientData] = useState(null);

  const sendMessage = async () => {
    if (!input) return;

    // Add user message
    setMessages((prev) => [
      ...prev,
      { text: input, sender: "user" }
    ]);

    try {
      const res = await fetch("https://ai-hospital-receptionists.onrender.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();

      console.log("BACKEND RESPONSE:", data);

      // Add bot reply
      setMessages((prev) => [
        ...prev,
        { text: data.message || "No response", sender: "bot" }
      ]);

      // ✅ FIXED: use backend name instead of guessing
      if (data.ward) {
        setPatientData({
          name: data.name,
          ward: data.ward
        });
      }

    } catch (error) {
      console.error("Error:", error);
    }

    setInput("");
  };

  // 🎨 Dynamic class for hospital vibe
  const getWardClass = () => {
    if (!patientData) return "";
    if (patientData.ward === "Emergency") return "card emergency";
    if (patientData.ward === "Mental Health") return "card mental";
    return "card general";
  };

  return (
    <div className="app">
      {/* 🏥 Chat Section */}
      <div className="chat-container">
        <h1>🏥 AI Hospital Receptionist</h1>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={msg.sender === "user" ? "user" : "bot"}
            >
              {msg.text}
            </div>
          ))}
        </div>

        <div className="input-area">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Describe your problem..."
          />
          <button onClick={sendMessage}>Send</button>
        </div>
      </div>

      {/* 💎 Patient Summary Card */}
      {patientData && (
        <div className={getWardClass()}>
          <h2>🧾 Patient Summary</h2>
          <p><strong>Name:</strong> {patientData.name}</p>
          <p><strong>Assigned Ward:</strong> {patientData.ward}</p>
        </div>
      )}
    </div>
  );
}

export default App;