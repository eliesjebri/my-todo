// frontend/src/components/AddTodo.js
import React, { useState } from "react";

export default function AddTodo({ onAdd }) {
  const [title, setTitle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    onAdd(title.trim());
    setTitle("");
  };

  return (
    <form onSubmit={handleSubmit} className="add-todo-form">
      <input
        type="text"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Ajouter une nouvelle tâche"
        className="add-todo-input"
      />
      <button type="submit" className="add-todo-button">Ajouter</button>
    </form>
  );
}
