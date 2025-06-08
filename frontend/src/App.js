// frontend/src/App.js

import React, { useEffect, useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTitle, setNewTitle] = useState("");
  const [version, setVersion] = useState(import.meta.env.VITE_FRONTEND_VERSION || "inconnue");

  const apiUrl = import.meta.env.VITE_API_URL;

  const fetchTodos = async () => {
    try {
      const res = await fetch(`${apiUrl}/todos`);
      const data = await res.json();
      setTodos(data);
    } catch (error) {
      console.error("Erreur lors du chargement des tâches :", error);
    }
  };

  const createTodo = async () => {
    if (!newTitle.trim()) return;
    try {
      const res = await fetch(`${apiUrl}/todos`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: newTitle }),
      });
      if (res.ok) {
        setNewTitle("");
        fetchTodos();
      }
    } catch (error) {
      console.error("Erreur lors de l'ajout :", error);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>📝 Ma Todo List</h1>

      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={newTitle}
          onChange={(e) => setNewTitle(e.target.value)}
          placeholder="Nouvelle tâche..."
        />
        <button onClick={createTodo} style={{ marginLeft: "1rem" }}>
          ➕ Ajouter
        </button>
      </div>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>✅ {todo.title}</li>
        ))}
      </ul>

      <footer style={{ marginTop: "2rem", fontSize: "0.9rem", color: "#666" }}>
        🌐 Frontend version : <strong>{version}</strong><br />
        🔗 API backend : <code>{apiUrl}</code>
      </footer>
    </div>
  );
}

export default App;
