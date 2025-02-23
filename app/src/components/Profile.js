import { useState, useEffect } from "react";
import io from "socket.io-client";
import "./Profile.css";

// Establece la conexión con el servidor Socket.IO
const socket = io("http://localhost:5000");

export default function Profile() {
  const [completedTasks, setCompletedTasks] = useState({});
  const [profileText, setProfileText] = useState("Recuerda beber agua hoy!");
  const [tasks, setTasks] = useState([]);

  // Alterna el estado de completado de una tarea
  const toggleTask = (index) => {
    setCompletedTasks((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  // Listener para recibir el perfil desde el backend
  useEffect(() => {
    socket.on("profileResponse", (data) => {
      if (data && data.text) {
        setProfileText(data.text);
      }
    });
    return () => {
      socket.off("profileResponse");
    };
  }, []);

  // Listener para recibir las tareas desde el backend
  useEffect(() => {
    socket.on("tasksResponse", (data) => {
      if (data && data.tasks) {
        // Separamos el string en líneas y filtramos las vacías
        const tasksArray = data.tasks.split("\n").filter((t) => t.trim() !== "");
        setTasks(tasksArray);
      }
    });
    return () => {
      socket.off("tasksResponse");
    };
  }, []);

  // Función para emitir el evento y recargar el perfil
  const cargarProfile = () => {
    socket.emit("cargarPerfil");
  };

  // Función para emitir el evento y recargar las tareas
  const cargarTareas = () => {
    socket.emit("cargarTareas");
  };

  return (
    <div>
      <h1>Emotional Profile</h1>
      <div className="container">
        {/* Sección del perfil */}
        <div className="profile-section">
          <div className="promptt">{profileText}</div>
        </div>

        {/* Sección de tareas */}
        <div className="todo-list">
          <h2>Tareas del día</h2>
          <ul className="task-list">
            {tasks.length > 0 ? (
              tasks.map((task, index) => (
                <li
                  key={index}
                  className="task-item"
                  onClick={() => toggleTask(index)}
                  style={{
                    textDecoration: completedTasks[index]
                      ? "line-through"
                      : "none",
                    color: completedTasks[index] ? "gray" : "black",
                    border: "1px solid #ccc",
                    padding: "10px",
                    textAlign: "center",
                    cursor: "pointer",
                    margin: "5px 0",
                  }}
                >
                  {task}
                </li>
              ))
            ) : (
              <li className="task-item">No hay tareas disponibles</li>
            )}
          </ul>
          <button className="profilebutton" onClick={cargarTareas}>
            Regenerar Tareas
          </button>
        </div>
      </div>
    </div>
  );
}
