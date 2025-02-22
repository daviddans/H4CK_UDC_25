import { useState } from "react";
import './Diary.css'

export default function Diary() {
  const [fechaSeleccionada, setFechaSeleccionada] = useState(new Date());
  const [entrada, setEntrada] = useState("");
  const [respuestas, setRespuestas] = useState({ q1: "", q2: ""});

  const guardarEntrada = () => {
    const fechaStr = fechaSeleccionada.toISOString().split("T")[0];
    localStorage.setItem(fechaStr, JSON.stringify({ entrada, respuestas }));
  };

  return (
    <div>
      <h1>Emotional Diary</h1>
      <div>
        <h2 class="fecha">{fechaSeleccionada.toDateString()}</h2>
        <input
          class="inputdate"
          type="date"
          value={fechaSeleccionada.toISOString().split("T")[0]}
          onChange={(e) => setFechaSeleccionada(new Date(e.target.value))}
        />
      </div>

      <textarea
        class="diarioentry"
        rows="6"
        placeholder="Escribe tu entrada del día..."
        value={entrada}
        onChange={(e) => setEntrada(e.target.value)}
      />

      <div>
        <label class="question">¿Qué harás mejor mañana?</label>
      </div>

      <div>
        {/* Posiblemente esto después habría que cambiarlo, porque solo queremos almacenar las respuestas actuales */}
        <input class="questionanswer" type="text" value={respuestas.q1} onChange={(e) => setRespuestas({ ...respuestas, q1: e.target.value })} />
      </div>

      <div>
        <label class="question">¿Qué aprendiste hoy?</label>
      </div>

      <div>
        <input class="questionanswer" type="text" value={respuestas.q2} onChange={(e) => setRespuestas({ ...respuestas, q2: e.target.value })} />
      </div>


      <button class="diarybutton"onClick={guardarEntrada}>
        Guardar
      </button>
    </div>
  );
}
