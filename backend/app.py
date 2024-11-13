from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime

app = Flask(__name__)
CORS(app)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://mongodb:27017/todoapp"
mongo = PyMongo(app)


@app.route("/api/todos", methods=["GET"])
def get_todos():
    todos = mongo.db.todos.find()
    return jsonify(
        [
            {
                "id": str(todo["_id"]),
                "title": todo["title"],
                "description": todo["description"],
                "status": todo["status"],
                "created_at": todo["created_at"],
            }
            for todo in todos
        ]
    )


@app.route("/api/todos", methods=["POST"])
def create_todo():
    data = request.json
    new_todo = {
        "title": data["title"],
        "description": data["description"],
        "status": "pending",
        "created_at": datetime.now(),
    }
    result = mongo.db.todos.insert_one(new_todo)
    return (
        jsonify(
            {"id": str(result.inserted_id), "message": "Todo created successfully"}
        ),
        201,
    )


@app.route("/api/todos/<todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json
    mongo.db.todos.update_one(
        {"_id": ObjectId(todo_id)},
        {
            "$set": {
                "title": data["title"],
                "description": data["description"],
                "status": data["status"],
            }
        },
    )
    return jsonify({"message": "Todo updated successfully"})


@app.route("/api/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    mongo.db.todos.delete_one({"_id": ObjectId(todo_id)})
    return jsonify({"message": "Todo deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
