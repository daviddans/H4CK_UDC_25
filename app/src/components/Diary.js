import { useState, useEffect } from "react";
import io from "socket.io-client";
import './Diary.css'

// Establece la conexión con el servidor Socket.IO
const socket = io("http://localhost:5000");

export default function Diary() {
  const [fechaSeleccionada, setFechaSeleccionada] = useState(new Date());
  const [entrada, setEntrada] = useState("");
  const [respuestas, setRespuestas] = useState({ q1: "", q2: ""});

  // Calcula la fecha actual en formato YYYY-MM-DD para comparar
  const todayStr = new Date().toISOString().split("T")[0];
  const fechaSeleccionadaStr = fechaSeleccionada.toISOString().split("T")[0];
  const isEditable = todayStr === fechaSeleccionadaStr;

  // Función para emitir el evento de carga del diario según la fecha
  const cargarEntrada = (fecha) => {
  socket.emit("cargaDiario", { fecha: fecha.toISOString().split("T")[0] });
  };

   // Al montar el componente, configuramos el listener para la respuesta del servidor
   useEffect(() => {
    socket.on("jsonResponse", (data) => {
      if (data.jsonResponse) {
        // Se espera que el objeto recibido tenga la estructura { entrada, respuestas }
        setEntrada(data.jsonResponse.entrada || "");
        setRespuestas(data.jsonResponse.respuestas || { q1: "", q2: "" });
      } else if (data.error) {
        setEntrada("");
        setRespuestas({ q1: "", q2: "" });
      }
    });
    return () => {
      socket.off("jsonResponse");
    };
  }, []);

  // Cada vez que se cambie la fecha seleccionada, se carga la entrada correspondiente
  useEffect(() => {
    cargarEntrada(fechaSeleccionada);
  }, [fechaSeleccionada]);

   // Función para guardar la entrada del diario
   const guardarEntrada = () => {
    const fechaStr = fechaSeleccionada.toISOString().split("T")[0];
    // Construir el objeto con las 3 entradas: la entrada principal y las 2 respuestas
    const datosDiario = {
      fecha: fechaStr,
      entrada,
      respuestas,
    };

    // Emitir el evento al servidor para guardar la entrada
    socket.emit("guardarDiario", datosDiario, (ack) => {
      if (ack.status === "ok") {
        console.log("Datos guardados correctamente en el servidor.");
      } else {
        console.error("Error al guardar en el servidor:", ack.error);
      }
    });
    
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
        readOnly={!isEditable}
      />

<div>
        <label className="question">¿Qué harás mejor mañana?</label>
      </div>
      <div>
        <input
          className="questionanswer"
          type="text"
          value={respuestas.q1}
          onChange={(e) => setRespuestas({ ...respuestas, q1: e.target.value })}
          readOnly={!isEditable}
        />
      </div>

      <div>
        <label className="question">¿Qué aprendiste hoy?</label>
      </div>
      <div>
        <input
          className="questionanswer"
          type="text"
          value={respuestas.q2}
          onChange={(e) => setRespuestas({ ...respuestas, q2: e.target.value })}
          readOnly={!isEditable}
        />
      </div>

      <button class="diarybutton"onClick={guardarEntrada}>
        Guardar
      </button>
    </div>
  );
}
