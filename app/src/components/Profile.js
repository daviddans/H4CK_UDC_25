import { useState, useEffect } from "react";
import "./Profile.css";

export default function Profile() {

    const [completedTasks, setCompletedTasks] = useState({});

    const toggleTask = (index) => {
        setCompletedTasks(prev => ({
            ...prev,
            [index]: !prev[index]  // Alterna entre `true` y `false`
        }));
    };

    const tasks = ["Tarea 1", "Tarea 2", "Tarea 3"];
    
      
    return (
        <div>
            <h1>Emotional Profile</h1>
            <div class="container">
        
                <div class="promptt">Recuerda beber agua hoy!</div>
                <div class="todo-list">
                <h2>Tareas del día</h2>
                <ul className="task-list">
                    {tasks.map((task, index) => (
                        <li 
                            key={index}
                            className="task-item"
                            onClick={() => toggleTask(index)}
                            style={{
                                textDecoration: completedTasks[index] ? "line-through" : "none",
                                color: completedTasks[index] ? "gray" : "black",
                                border: "1px solid #ccc",
                                padding: "10px",
                                textAlign: "center",
                                cursor: "pointer",
                                margin: "5px 0"
                            }}
                        >
                            {task}
                        </li>
                    ))}
                </ul>

                <button class="profilebutton"onClick={null}>
                    Recargar tareas
                </button>

                </div>
            </div>
        </div>
    );
}
    