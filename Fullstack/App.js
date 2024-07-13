// App.js
import React, { useState, useEffect } from 'react';
import DishCard from './DishCard';

function App() {
    const [dishes, setDishes] = useState([]);

    useEffect(() => {
        fetch('/dishes')
            .then(response => response.json())
            .then(data => setDishes(data));
    }, []);

    const togglePublish = (dishId) => {
        fetch(`/toggle-publish/${dishId}`, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                setDishes(dishes.map(dish =>
                    dish.dishId === dishId ? { ...dish, isPublished: data.newStatus } : dish
                ));
            });
    };

    return (
        <div className="App">
            <h1>Dishes Dashboard</h1>
            <div className="dish-list">
                {dishes.map(dish => (
                    <DishCard key={dish.dishId} dish={dish} togglePublish={togglePublish} />
                ))}
            </div>
        </div>
    );
}

export default App;
