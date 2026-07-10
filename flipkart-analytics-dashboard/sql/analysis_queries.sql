SELECT brand, COUNT(*) AS total_reviews
FROM reviews
GROUP BY brand
ORDER BY total_reviews DESC;

SELECT brand, AVG(rating) AS avg_rating
FROM reviews
GROUP BY brand
ORDER BY avg_rating DESC;

SELECT sentiment, COUNT(*) AS count
FROM reviews
GROUP BY sentiment;

SELECT product_name, review_length
FROM reviews
ORDER BY review_length DESC
LIMIT 10;

SELECT product_name, AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_name
ORDER BY avg_rating DESC
LIMIT 10;

