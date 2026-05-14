
SELECT restaurant_name,
       rating
FROM restaurants
ORDER BY rating DESC
LIMIT 10;


SELECT COUNT(*) AS online_restaurants
FROM restaurants
WHERE online_order = TRUE;



SELECT restaurant_type,
       AVG(approx_cost) AS avg_cost
FROM restaurants
GROUP BY restaurant_type
ORDER BY avg_cost DESC;



SELECT restaurant_name,
       votes
FROM restaurants
ORDER BY votes DESC
LIMIT 10;



SELECT restaurant_name,
       restaurant_type,
       rating,
       RANK() OVER (
           PARTITION BY restaurant_type
           ORDER BY rating DESC
       ) AS rank
FROM restaurants;



SELECT restaurant_name,
       rating,
       DENSE_RANK() OVER (
           ORDER BY rating DESC
       ) AS dense_rank
FROM restaurants;



SELECT restaurant_name,
       rating
FROM restaurants
WHERE rating > (
    SELECT AVG(rating)
    FROM restaurants
);


SELECT restaurant_type,
       COUNT(*) AS total_restaurants
FROM restaurants
GROUP BY restaurant_type
HAVING COUNT(*) > 5;


SELECT restaurant_name,
       approx_cost
FROM restaurants
ORDER BY approx_cost DESC
LIMIT 10;