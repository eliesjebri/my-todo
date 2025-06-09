import React from "react";

function TodoItem({ todo, onToggleComplete, onDelete }) {
  return (
    <li className="flex justify-between items-center p-2 border-b">
      <div className="flex items-center space-x-2">
        <input
          type="checkbox"
          checked={todo.completed}
          onChange={() => onToggleComplete(todo.id)}
          className="form-checkbox h-5 w-5 text-blue-600"
        />
        <span className={todo.completed ? "line-through text-gray-400" : ""}>
          {todo.title}
        </span>
      </div>
      <button
        onClick={() => onDelete(todo.id)}
        className="text-red-500 hover:text-red-700"
      >
        Supprimer
      </button>
    </li>
  );
}

export default TodoItem;
