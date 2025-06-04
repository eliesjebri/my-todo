from flask import Blueprint, request, jsonify
from src.services.todo_service import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    complete_task,
    delete_task
)
from src.config import Config

todos_bp = Blueprint("todos", __name__)

# 🔹 Health check
@todos_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok"}), 200

# 🔹 Version
@todos_bp.route("/version", methods=["GET"])
def version():
    return jsonify({"version": Config.VERSION}), 200

# 🔹 GET /todos — liste toutes les tâches
@todos_bp.route("/todos", methods=["GET"])
def list_todos():
    tasks = get_all_tasks()
    return jsonify(tasks), 200

# 🔹 POST /todos — créer une tâche
@todos_bp.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Le champ 'title' est requis."}), 400

    task = create_task(data["title"])
    return jsonify(task), 201

# 🔹 PUT /todos/:id — modifier une tâche
@todos_bp.route("/todos/<int:task_id>", methods=["PUT"])
def edit_todo(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Tâche non trouvée."}), 404

    data = request.get_json()
    updated = update_task(task_id, title=data.get("title"))
    return jsonify(updated), 200

# 🔹 PATCH /todos/:id/complete — marquer comme complétée
@todos_bp.route("/todos/<int:task_id>/complete", methods=["PATCH"])
def complete(task_id):
    updated = complete_task(task_id)
    if not updated:
        return jsonify({"error": "Tâche non trouvée."}), 404
    return jsonify(updated), 200

# 🔹 DELETE /todos/:id — supprimer une tâche
@todos_bp.route("/todos/<int:task_id>", methods=["DELETE"])
def remove_todo(task_id):
    deleted = delete_task(task_id)
    if not deleted:
        return jsonify({"error": "Tâche non trouvée."}), 404
    return jsonify({"message": "Tâche supprimée."}), 200
