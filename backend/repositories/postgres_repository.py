from .base_repository import BaseRepository
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class PostgresRepository(BaseRepository):
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def find_all(self):
        todos = self.session.query(Todo).all()
        return [
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "status": todo.status,
                "created_at": todo.created_at,
            }
            for todo in todos
        ]

    def insert_one(self, data):
        todo = Todo(
            title=data["title"],
            description=data["description"],
            status=data["status"],
            created_at=data["created_at"],
        )
        self.session.add(todo)
        self.session.commit()
        return {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "status": todo.status,
            "created_at": todo.created_at,
        }

    def update_one(self, id, data):
        todo = self.session.query(Todo).filter_by(id=id).first()
        if todo:
            todo.title = data["title"]
            todo.description = data["description"]
            todo.status = data["status"]
            self.session.commit()
        return (
            {
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "status": todo.status,
                "created_at": todo.created_at,
            }
            if todo
            else None
        )

    def delete_one(self, id):
        todo = self.session.query(Todo).filter_by(id=id).first()
        if todo:
            self.session.delete(todo)
            self.session.commit()
            return True
        return False
