import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

# from flask_pymongo import PyMongo
# from repositories.mongo_repository import MongoRepository

from repositories.postgres_repository import PostgresRepository

app = Flask(__name__)
CORS(app)

# MongoDB
# app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# mongo = PyMongo(app)
# repo = MongoRepository(mongo)

# Postgres
db_url = os.environ.get("POSTGRES_URL")
repo = PostgresRepository(db_url)


@app.route("/api/todos", methods=["GET"])
def get_todos():
    todos = repo.find_all()
    return jsonify(
        [
            {
                "id": str(todo["id"]),
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
    result = repo.insert_one(new_todo)
    return (
        jsonify({"id": str(result["id"]), "message": "Todo created successfully"}),
        201,
    )


@app.route("/api/todos/<todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json

    repo.update_one(
        todo_id,
        {
            "title": data["title"],
            "description": data["description"],
            "status": data["status"],
        },
    )

    return jsonify({"message": "Todo updated successfully"})


@app.route("/api/todos/<todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    repo.delete_one(todo_id)
    return jsonify({"message": "Todo deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
