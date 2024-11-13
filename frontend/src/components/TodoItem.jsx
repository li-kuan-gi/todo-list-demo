import React, { useState } from 'react';

const TodoItem = ({ todo, onUpdate, onDelete }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [editTitle, setEditTitle] = useState(todo.title);
    const [editDescription, setEditDescription] = useState(todo.description);

    const handleUpdate = () => {
        onUpdate(todo.id, {
            ...todo,
            title: editTitle,
            description: editDescription
        });
        setIsEditing(false);
    };

    const toggleStatus = () => {
        onUpdate(todo.id, {
            ...todo,
            status: todo.status === 'pending' ? 'completed' : 'pending'
        });
    };

    if (isEditing) {
        return (
            <div className="p-4 border rounded">
                <input
                    type="text"
                    value={editTitle}
                    onChange={(e) => setEditTitle(e.target.value)}
                    className="w-full p-2 border rounded mb-2"
                />
                <textarea
                    value={editDescription}
                    onChange={(e) => setEditDescription(e.target.value)}
                    className="w-full p-2 border rounded mb-2"
                />
                <div className="flex space-x-2">
                    <button
                        onClick={handleUpdate}
                        className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
                    >
                        Save
                    </button>
                    <button
                        onClick={() => setIsEditing(false)}
                        className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                    >

                        Cancel
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="p-4 border rounded flex items-center justify-between">
            <div className="flex items-center space-x-4">
                <input
                    type="checkbox"
                    checked={todo.status === 'completed'}
                    onChange={toggleStatus}
                    className="h-4 w-4"
                />
                <div>
                    <h3 className={`font-semibold ${todo.status === 'completed' ? 'line-through' : ''}`}>
                        {todo.title}
                    </h3>
                    {todo.description && (
                        <p className="text-gray-600">{todo.description}</p>
                    )}
                </div>
            </div>
            <div className="flex space-x-2">
                <button
                    onClick={() => setIsEditing(true)}
                    className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
                >
                    Edit
                </button>

                <button
                    onClick={() => onDelete(todo.id)}
                    className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
                >
                    Delete
                </button>
            </div>
        </div>
    );
};

export default TodoItem;