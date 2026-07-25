from flask import Blueprint,jsonify,request
from flask_restx import Api

task_bp = Blueprint("task",__name__)


tasks = []

@task_bp.route("/tasks",methods=["Get"])
def get_task():
    return jsonify(tasks),200

@task_bp.route("/get/tasks/<int:id>",methods=["Get"])
def get_task_id(id):
    for task in tasks:
        if task["id"] == id:
            return jsonify(task),200
    return jsonify({
        "message": f"task not found {id}"
    }),404

@task_bp.route("/add/task", methods = ["Post"])
def add_task():
    data = request.get_json()
    tasks.append({
        "id": len(tasks) + 1,
        "title":data["title"],
        "completed":data["completed"]
    })

    return jsonify({
        "message": "Add succussfully"
    }),201

@task_bp.route("/repalce/task/<int:id>", methods = ["Put"])
def replace_task(id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == id:
            task["title"] = data["title"]
            task["completed"] = data["completed"]
            return jsonify({
                "message": "replace succufully"
            }),200
    return jsonify({
        "message": "Task not found"
    }),404


@task_bp.route("/update/task/<int:id>", methods = ["Patch"])
def update_task(id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == id:
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed",task["completed"])
            return jsonify({
                "message": "upadte succufully"
            }),200
    return jsonify({
        "message": "Task not found"
    }),404

@task_bp.route("/delete/task/<int:id>", methods = ["Delete"])
def remove_task(id):

    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return jsonify({
                "message": "delete succufully"
            }),200
    return jsonify({
        "message": "Task not found"
    }),404