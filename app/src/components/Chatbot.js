import './Chatbot.css'
import { useState } from "react";

// Creamos el componente Chatbot
export default function Chatbot() {

  // messages -> almacenamos los mensajes enviados en el chat (incialmente es un array vacío) [estado actual]
  // setMessages -> es la función que usamos para actualizar los mensajes [permite actualizar el estado actual]
  // useState -> establece el valor inicial como un array vacío []
  const [messages, setMessages] = useState([]);

  // input -> almacena el valor del cuadro de texto donde el usuario escribe [estado actual]
  // setInput -> es la función para almacenar el valor del cuadro de texto [permite actualizar el estado actual]
  // useState -> establece el valor inicial como un array vacío []
  const [input, setInput] = useState("");

  // Función para enviar un mensaje
  const sendMessage = () => {

    // En caso de que el input esté vacío, no hace nada
    if (!input.trim()) return;

    //Si no está vacío, con setMessages agregamos un nuevo mensaje al array
    // ...messages -> "copia" todos los mensajes del estado anterior
    // { text: input, sender: "user" } -> es el nuevo mensaje
    //setMessages -> junta el anterior estado con el nuevo mensaje y actualiza el estado
    setMessages([{ text: input, sender: "user" }, ...messages]);

    //Cuando el mensaje ha sido enviado, limpiamos el cuadro de texto
    setInput("");
  };

  return (

    //Para diseñar el contenedor del chat
    <div class="chat">

    <h1>Emotional ChatBot</h1>

    {/* Contenendor de Mensajes */}

      <div class="chat-container">
        
        {/* Recorremos el array de mensajes con messages.map */}
        {/* msg -> representa cada mensaje individual en la interación */}
        {/* index -> es el número de posición de cada mensaje en el array */}
        {messages.map((msg, index) => (
          <div class="message user-message">
            {msg.text}
          </div>
        ))}
      </div>

        {/* Input y boton para enviar mensajes */}
      <div class="prompt">

        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
          placeholder="Escribe un mensaje..."
        />

        <button onClick={sendMessage}>
          Enviar
        </button>
        
      </div>

    </div>
  );
}
