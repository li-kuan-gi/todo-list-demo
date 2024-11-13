import React, { useState, useEffect } from 'react';
import TodoForm from './components/TodoForm';
import TodoList from './components/TodoList';
import axios from 'axios';

const App = () => {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        fetchTodos();
    }, []);

    const fetchTodos = async () => {
        try {
            const response = await axios.get('http://localhost:5000/api/todos');
            setTodos(response.data);
        } catch (error) {
            console.error('Error fetching todos:', error);
        }
    };

    const addTodo = async (todo) => {
        try {
            await axios.post('http://localhost:5000/api/todos', todo);
            fetchTodos();
        } catch (error) {
            console.error('Error adding todo:', error);
        }
    };

    const updateTodo = async (id, updatedTodo) => {
        try {
            await axios.put(`http://localhost:5000/api/todos/${id}`, updatedTodo);
            fetchTodos();
        } catch (error) {
            console.error('Error updating todo:', error);
        }
    };


    const deleteTodo = async (id) => {
        try {
            await axios.delete(`http://localhost:5000/api/todos/${id}`);
            fetchTodos();
        } catch (error) {
            console.error('Error deleting todo:', error);
        }
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold mb-8 text-center">Todo List</h1>
            <TodoForm onSubmit={addTodo} />
            <TodoList
                todos={todos}
                onUpdate={updateTodo}
                onDelete={deleteTodo}
            />
        </div>
    );
};

export default App;