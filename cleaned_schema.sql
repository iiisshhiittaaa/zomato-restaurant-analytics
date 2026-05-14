CREATE TABLE restaurants (
    restaurant_id SERIAL PRIMARY KEY,
    restaurant_name VARCHAR(255),
    online_order BOOLEAN,
    book_table BOOLEAN,
    rating FLOAT,
    votes INT,
    approx_cost INT,
    restaurant_type VARCHAR(100)
);