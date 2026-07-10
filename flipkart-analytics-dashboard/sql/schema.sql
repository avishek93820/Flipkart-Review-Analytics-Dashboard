USE flipkart_reviews;
CREATE TABLE reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name TEXT,
    brand VARCHAR(100),
    review TEXT,
    rating INT,
    review_length INT,
    rating_label VARCHAR(20),
    sentiment VARCHAR(20)
);