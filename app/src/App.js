import React, { useState } from "react";
import Chatbot from "./components/Chatbot";
import './App.css';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  return (
    <div className="App">
      <div className="container">
        {/* Menú lateral minimalista */}
        <div className={`sidebar ${isSidebarOpen ? "open" : "closed"}`}>
          <button 
            className="toggle-btn" 
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          >
            {isSidebarOpen ? "←" : "→"}
          </button>
          {isSidebarOpen && (
            <div className="menu">
              <ul>
                <li>Chat</li>
                <li>Diario</li>
                <li>Perfil</li>
              </ul>
            </div>
          )}
        </div>

        {/* Área principal de contenido */}
        <div className="main-content">
          <Chatbot />
        </div>
      </div>
    </div>
  );
}

export default App;
