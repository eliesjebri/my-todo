const API_URL = "http://todo-staging:5001"; // ⚠️ Adapter selon le nom du service en Docker

async function fetchTodos() {
  const res = await fetch(`${API_URL}/todos`);
  const todos = await res.json();
  const list = document.getElementById("todo-list");
  list.innerHTML = "";
  todos.forEach((todo) => {
    const li = document.createElement("li");
    li.textContent = todo.title + (todo.done ? " ✅" : "");
    list.appendChild(li);
  });
}

async function addTodo() {
  const input = document.getElementById("new-todo");
  const title = input.value;
  if (!title) return;

  await fetch(`${API_URL}/todos`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  input.value = "";
  fetchTodos();
}

window.onload = fetchTodos;
