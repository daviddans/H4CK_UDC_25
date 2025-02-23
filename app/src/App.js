import React, { useState } from "react";
import Chatbot from "./components/Chatbot";
import Diary from "./components/Diary";
import Profile from "./components/Profile";
import './App.css';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [activeSection, setActiveSection] = useState("chat"); // Estado para la sección activa

  // Función para cambiar la sección activa
  const handleMenuClick = (section) => {
    setActiveSection(section);
    setIsSidebarOpen(false); // Cierra el menú después de hacer clic (opcional)
  };

  return (
    <div class="App">
      <div class="containerr">
        {/* Menú lateral */}
        <div class={`sidebar ${isSidebarOpen ? "open" : "closed"}`}>
          <button 
            class="toggle-btn" 
            onClick={() => setIsSidebarOpen(!isSidebarOpen)}
          >
            {isSidebarOpen ? "←" : "→"}
          </button>
          {isSidebarOpen && (
            <div class="menu">
              <ul>
                <li onClick={() => handleMenuClick("chat")}>ChatBot</li>
                <li onClick={() => handleMenuClick("diario")}>Diary</li>
                <li onClick={() => handleMenuClick("perfil")}>Profile</li>
              </ul>
            </div>
          )}
        </div>

        {/* Contenido dinámico */}
        <div class="main-content">
          {activeSection === "chat" && <Chatbot />}
          {activeSection === "diario" && <Diary />}
          {activeSection === "perfil" && <Profile />}
        </div>
      </div>
    </div>
  );
}

export default App;
