from flask import Blueprint,jsonify,request
from flask_restx import Api,Resource,fields

task_bp = Blueprint("task",__name__)

api = Api(
    task_bp,
    title="Todo API",
    version="1.0",
    description="CRUD API for tasks"
)

task_model = api.model("Task", {
    "title": fields.String(required=False),
    "completed": fields.Boolean(required=False)
})

tasks = []

@api.route("/tasks")
class TaskList(Resource):
    def get(self):
        return tasks,200

    @api.expect(task_model, validate=True)
    def post(self):
        data = request.get_json()
        tasks.append({
            "id": len(tasks) + 1,
            "title":data["title"],
            "completed":data["completed"]
            })
        return {"message":"Add Succufully"},201

    
@api.route("/tasks/<int:id>")
class Task(Resource):
    def get(self, id):
        for task in tasks:
            if task["id"] == id:
                return task,200
        return {"message": f"task not found {id}"},404

    @api.expect(task_model, validate=True)
    def put(self, id):
        data = request.get_json()
        for task in tasks:
            if task["id"] == id:
                task["title"] = data["title"]
                task["completed"] = data["completed"]
                return {
                    "message": "replace succufully"
                    },200
        return {
            "message": "Task not found"
        },404

    @api.expect(task_model, validate=True)
    def patch(self, id):
        data = request.get_json()
        for task in tasks:
            if task["id"] == id:
                task["title"] = data.get("title", task["title"])
                task["completed"] = data.get("completed",task["completed"])
                return {
                    "message": "upadte succufully"
                    },200
        return {
            "message": "Task not found"
            },404

    def delete(self,id):
        for task in tasks:
            if task["id"] == id:
                tasks.remove(task)
                return {
                    "message": "delete succufully"
                    },200
        return {
            "message": "Task not found"
            },404