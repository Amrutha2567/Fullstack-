// DishCard.js
import React from 'react';

function DishCard({ dish, togglePublish }) {
    return (
        <div className="dish-card">
            <img src={dish.imageUrl} alt={dish.dishName} />
            <h2>{dish.dishName}</h2>
            <button onClick={() => togglePublish(dish.dishId)}>
                {dish.isPublished ? 'Unpublish' : 'Publish'}
            </button>
        </div>
    );
}

export default DishCard;
