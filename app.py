from flask import Flask
from routes.task_routes import task_bp
from database import init_db

app = Flask(__name__)

init_db()

@app.route("/health")
def health():
    return "toDo api is working"

app.register_blueprint(task_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)