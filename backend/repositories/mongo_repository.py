from .base_repository import BaseRepository
from bson import ObjectId
from datetime import datetime


class MongoRepository(BaseRepository):
    def __init__(self, mongo_client):
        self.db = mongo_client.db.todos

    def find_all(self):
        todos = self.db.find()
        return [
            {
                "id": str(todo["_id"]),
                "title": todo["title"],
                "description": todo["description"],
                "status": todo["status"],
                "created_at": todo["created_at"],
            }
            for todo in todos
        ]

    def insert_one(self, data):
        todo_data = {
            "title": data["title"],
            "description": data["description"],
            "status": data["status"],
            "created_at": data["created_at"],
        }
        result = self.db.insert_one(todo_data)
        return {"id": str(result.inserted_id), **todo_data}

    def update_one(self, id, data):
        todo_data = {
            "title": data["title"],
            "description": data["description"],
            "status": data["status"],
        }
        self.db.update_one({"_id": ObjectId(id)}, {"$set": todo_data})
        return {"id": id, **todo_data}

    def delete_one(self, id):
        result = self.db.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
