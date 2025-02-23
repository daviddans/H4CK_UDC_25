import { useState, useEffect } from "react";
import "./Profile.css";

export default function Profile() {
      
    return (
        <div>
            <h1>Emotional Profile</h1>
            <div class="container">
        
                <div class="promptt">Recuerda beber agua hoy!</div>
                <div class="todo-list">
                <h2>Tareas del día</h2>
                <ul class="task-list">
                    <li class="task-item">
                        Tarea 1
                    </li>
                    <li className="task-item">
                        Tarea 2
                    </li>
                    <li className="task-item">
                        Tarea 3
                    </li>
                </ul>

                <button class="profilebutton"onClick={null}>
                    Recargar tareas
                </button>

                </div>
            </div>
        </div>
    );
}
    