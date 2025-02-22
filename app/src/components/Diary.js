import { useState, useEffect } from "react";
import './Diary.css'

export default function Diario() {
  const [fechaSeleccionada, setFechaSeleccionada] = useState(new Date());
  const [entrada, setEntrada] = useState("");
  const [respuestas, setRespuestas] = useState({ q1: "", q2: ""});

  useEffect(() => {
    const fechaStr = fechaSeleccionada.toISOString().split("T")[0];
    const datosGuardados = JSON.parse(localStorage.getItem(fechaStr)) || { entrada: "", respuestas: { q1: "", q2: ""} };
    setEntrada(datosGuardados.entrada);
    setRespuestas(datosGuardados.respuestas);
  }, [fechaSeleccionada]);

  const guardarEntrada = () => {
    const fechaStr = fechaSeleccionada.toISOString().split("T")[0];
    localStorage.setItem(fechaStr, JSON.stringify({ entrada, respuestas }));
  };

  return (
    <div>
      <div>
        <h2>{fechaSeleccionada.toDateString()}</h2>
        <input
          type="date"
          value={fechaSeleccionada.toISOString().split("T")[0]}
          onChange={(e) => setFechaSeleccionada(new Date(e.target.value))}
        />
      </div>

      <textarea
        rows="6"
        placeholder="Escribe tu entrada del día..."
        value={entrada}
        onChange={(e) => setEntrada(e.target.value)}
      />

      <div>
        <label>¿Qué harás mejor mañana?</label>
      </div>

      <div>
        {/* Posiblemente esto después habría que cambiarlo, porque solo queremos almacenar las respuestas actuales */}
        <input type="text" value={respuestas.q1} onChange={(e) => setRespuestas({ ...respuestas, q1: e.target.value })} />
      </div>

      <div>
        <label>¿Qué aprendiste hoy?</label>
      </div>

      <div>
        <input type="text" value={respuestas.q2} onChange={(e) => setRespuestas({ ...respuestas, q2: e.target.value })} />
      </div>


      <button onClick={guardarEntrada}>
        Guardar
      </button>
    </div>
  );
}
