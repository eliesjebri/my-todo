// frontend/src/services/todoService.js
import { API_URL } from "./config";

const headers = {
  "Content-Type": "application/json",
};

export async function getTodos() {
  const response = await fetch(`${API_URL}/todos`);
  return response.json();
}

export async function addTodo(title) {
  const response = await fetch(`${API_URL}/todos`, {
    method: "POST",
    headers,
    body: JSON.stringify({ title }),
  });
  return response.json();
}

export async function deleteTodo(id) {
  const response = await fetch(`${API_URL}/todos/${id}`, {
    method: "DELETE",
    headers,
  });
  return response.ok;
}

export async function toggleTodo(id, done) {
  const response = await fetch(`${API_URL}/todos/${id}`, {
    method: "PATCH",
    headers,
    body: JSON.stringify({ done }),
  });
  return response.json();
}
