CREATE DATABASE zomato_db;
CREATE TABLE zomato_raw (
    restaurant_name VARCHAR(255),
    online_order VARCHAR(10),
    book_table VARCHAR(10),
    rate VARCHAR(20),
    votes INT,
    approx_cost VARCHAR(20),
    listed_in_type VARCHAR(100)
);