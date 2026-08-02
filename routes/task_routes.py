from flask import Blueprint,jsonify,request
from flask_restx import Api,Resource,fields
from database import conn,cursor

task_bp = Blueprint("task",__name__)

api = Api(
    task_bp,
    title="Todo API",
    version="1.0",
    description="CRUD API for tasks"
)

task_model = api.model("Task", {
    "title": fields.String(required=True),
    "completed": fields.Boolean(required=True)
})

update_model = api.model("UpdateTask", {
    "title": fields.String(required=False),
    "completed": fields.Boolean(required=False)
})


@api.route("/tasks")
class TaskList(Resource):
    def get(self):
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()

        return tasks,200
    
    @api.expect(task_model, validate=True)
    def post(self):
        data = request.get_json()
        cursor.execute("INSERT INTO tasks (title, completed) VALUES (?,?)", (data["title"], data["completed"]))
        conn.commit()
        return {"message":"Add Succufully"},201

    
@api.route("/tasks/<int:id>")
class Task(Resource):
    def get(self, id):
        cursor.execute("SELECT * FROM tasks WHERE ID = ?",(id,))
        task = cursor.fetchone()

        if(task is None):
            return {"message": f"task not found {id}"},404
        
        return {
            "id": task[0],
            "title": task[1],
            "completed": bool(task[2])
        }, 200    

    @api.expect(task_model, validate=True)
    def put(self, id):
        data = request.get_json()

        cursor.execute("SELECT * FROM tasks WHERE id = ?",(id,))
        task = cursor.fetchone()

        if(task is None):
            return {"message": f"task not found {id}"},404
        
        cursor.execute("UPDATE tasks SET title = ?, completed = ? WHERE id = ?", (data["title"], data["completed"], id))

        conn.commit()

        return {
            "message" : "Update Succufully"
        },200

        
    @api.expect(update_model, validate=True)
    def patch(self, id):
        data = request.get_json()

        cursor.execute("SELECT * FROM tasks WHERE id = ?",(id,))

        task = cursor.fetchone()
        
        if(task is None):
            return {"message": f"task not found {id}"},404
        
        title = task[1]
        completed = task[2]
        cursor.execute("UPDATE tasks SET title = ?, completed = ? WHERE id = ?", (data.get("title",title), data.get("completed", completed), id))

        conn.commit()

        return {
            "message" : "Update Succufully"
            },200

    def delete(self, id):

        cursor.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (id,)
        )
        task = cursor.fetchone()

        if task is None:
            return {
                "message": "Task not found"
            }, 404

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (id,)
        )

        conn.commit()

        return {
            "message": "Task deleted successfully"
        }, 200