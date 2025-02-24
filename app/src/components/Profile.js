import { useState, useEffect } from "react";
import io from "socket.io-client";
import "./Profile.css";

// Establece la conexión con el servidor Socket.IO
const socket = io("http://localhost:5000");

export default function Profile() {
  const [completedTasks, setCompletedTasks] = useState({});
  const [profileText, setProfileText] = useState("Recuerda beber agua hoy!");
  const [tasks, setTasks] = useState([]);
  const [loadingTasks, setLoadingTasks] = useState(false); // Estado para deshabilitar el botón

  // Alterna el estado de completado de una tarea
  const toggleTask = (index) => {
    setCompletedTasks((prev) => ({
      ...prev,
      [index]: !prev[index],
    }));
  };

  // Listener para recibir el perfil desde el backend
  useEffect(() => {
    socket.emit("cargarPerfil");
    socket.on("profileResponse", (data) => {
      if (data && data.text) {
        setProfileText(data.text);
      }
    });
    return () => {
      socket.off("profileResponse");
    };
  }, []);

  // Listener para recibir las tareas (tanto al cargar como al regenerar)
  useEffect(() => {
    socket.emit("loadTasks");

    const handleTasksResponse = (data) => {
      if (data && data.tasks) {
        const tasksArray = data.tasks.split("\n").filter((t) => t.trim() !== "");
        setTasks(tasksArray);
        setLoadingTasks(false); // Habilita el botón cuando llegan las tareas
      }
    };

    // Escuchar eventos tanto para la carga inicial como para la regeneración
    socket.on("tasksLoadResponse", handleTasksResponse);
    socket.on("tasksResponse", handleTasksResponse);

    return () => {
      socket.off("tasksLoadResponse", handleTasksResponse);
      socket.off("tasksResponse", handleTasksResponse);
    };
  }, []);

  // Función para generar nuevas tareas
  const cargarTareas = () => {
    if (loadingTasks) return;
    setLoadingTasks(true); // Deshabilita el botón
    socket.emit("generateTasks"); // Se envía al backend para regenerar tareas
  };

  // Función para convertir `**texto**` en `<b>texto</b>`
  const formatText = (text) => {
    return text.replace(/\*\*(.*?)\*\*/g, "<b>$1</b>"); // Reemplaza `**negrita**` por `<b>negrita</b>`
  };

  return (
    <div>
      <h1>Emotional Profile</h1>
      <div className="container">
        <div className="profile-section">
          <div className="promptt">{profileText}</div>
        </div>

        <div className="todo-list">
          <h2>Tareas del día</h2>
          <ul className="task-list">
            {tasks.length > 0 ? (
              tasks.map((task, index) => (
                <li
                  key={index}
                  className="task-item"
                  onClick={() => setCompletedTasks((prev) => ({ ...prev, [index]: !prev[index] }))}
                  style={{
                    textDecoration: completedTasks[index] ? "line-through" : "none",
                    color: completedTasks[index] ? "gray" : "black",
                    border: "1px solid #ccc",
                    padding: "10px",
                    textAlign: "center",
                    cursor: "pointer",
                    margin: "5px 0",
                  }}
                  dangerouslySetInnerHTML={{ __html: formatText(task) }} // Convierte texto a HTML
                ></li>
              ))
            ) : (
              <li className="task-item">No hay tareas disponibles</li>
            )}
          </ul>
          <button
            className="tasksbutton"
            onClick={cargarTareas}
            disabled={loadingTasks} // Deshabilita el botón mientras está cargando
            style={{
              backgroundColor: loadingTasks ? "#ccc" : "#007bff",
              cursor: loadingTasks ? "not-allowed" : "pointer",
            }}
          >
            {loadingTasks ? "Generando..." : "Regenerar Tareas"}
          </button>
        </div>
      </div>
    </div>
  );
}
