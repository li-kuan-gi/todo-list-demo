from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """
    'data' is a dictionary containing the fields (optional):
        'title': title of the todo
        'description': description of the todo
        'status': status of the todo ('pending', 'completed')
        'created_at': date and time when the todo was created
    """

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def insert_one(self, data):
        pass

    @abstractmethod
    def update_one(self, id, data):
        pass

    @abstractmethod
    def delete_one(self, id):
        pass
