CREATE DATABASE airbnb_analysis;
USE airbnb_analysis;

CREATE TABLE airbnb_listings (
    listing_id BIGINT PRIMARY KEY,
    listing_name VARCHAR(255),
    host_id BIGINT,
    host_name VARCHAR(100),
    borough VARCHAR(100),
    neighbourhood VARCHAR(100),
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    room_type VARCHAR(100),
    price_usd DECIMAL(10,2),
    minimum_nights INT,
    number_of_reviews INT,
    reviews_per_month DECIMAL(10,2),
    review_score DECIMAL(4,2),
    availability_365 INT,
    number_of_reviews_ltm INT,
    calculated_host_listings_count INT,
    instant_bookable VARCHAR(10),
    host_response_rate_pct DECIMAL(5,2),
    property_type VARCHAR(100),
    accommodates INT,
    beds INT,
    bathrooms DECIMAL(4,1),
    price_category VARCHAR(50),
    availability_category VARCHAR(50),
    host_type VARCHAR(50),
    estimated_annual_revenue_usd DECIMAL(15,2)
);

-- Q1. Total listings
SELECT COUNT(*) AS total_listings
FROM airbnb_listings;


-- Q2. Total hosts
SELECT COUNT(DISTINCT host_id) AS total_hosts
FROM airbnb_listings;


-- Q3. Average price
SELECT ROUND(AVG(price_usd), 2) AS average_price
FROM airbnb_listings;


-- Q4. Minimum and maximum price
SELECT
    MIN(price_usd) AS minimum_price,
    MAX(price_usd) AS maximum_price
FROM airbnb_listings;


-- Q5. Listings by borough
SELECT
    borough,
    COUNT(*) AS total_listings
FROM airbnb_listings
GROUP BY borough
ORDER BY total_listings DESC;


-- Q6. Average price by borough
SELECT
    borough,
    ROUND(AVG(price_usd), 2) AS avg_price
FROM airbnb_listings
GROUP BY borough
ORDER BY avg_price DESC;


-- Q7. Average price by room type
SELECT
    room_type,
    ROUND(AVG(price_usd), 2) AS avg_price
FROM airbnb_listings
GROUP BY room_type
ORDER BY avg_price DESC;


-- Q8. Listings by room type
SELECT
    room_type,
    COUNT(*) AS listings
FROM airbnb_listings
GROUP BY room_type
ORDER BY listings DESC;


-- Q9. Average reviews by borough
SELECT
    borough,
    ROUND(AVG(number_of_reviews), 2) AS avg_reviews
FROM airbnb_listings
GROUP BY borough
ORDER BY avg_reviews DESC;


-- Q10. Top 10 neighborhoods by listings
SELECT
    neighbourhood,
    COUNT(*) AS total_listings
FROM airbnb_listings
GROUP BY neighbourhood
ORDER BY total_listings DESC
LIMIT 10;


-- Q11. Top 10 expensive neighborhoods
SELECT
    neighbourhood,
    ROUND(AVG(price_usd), 2) AS avg_price
FROM airbnb_listings
GROUP BY neighbourhood
HAVING COUNT(*) >= 10
ORDER BY avg_price DESC
LIMIT 10;


-- Q12. Listings with rating above 4.8
SELECT
    COUNT(*) AS highly_rated_listings
FROM airbnb_listings
WHERE review_score >= 4.8;


-- Q13. Average rating by borough
SELECT
    borough,
    ROUND(AVG(review_score), 2) AS avg_rating
FROM airbnb_listings
GROUP BY borough
ORDER BY avg_rating DESC;


-- Q14. Instant-bookable listings
SELECT
    instant_bookable,
    COUNT(*) AS total_listings
FROM airbnb_listings
GROUP BY instant_bookable;


-- Q15. Average availability by borough
SELECT
    borough,
    ROUND(AVG(availability_365), 2) AS avg_available_days
FROM airbnb_listings
GROUP BY borough
ORDER BY avg_available_days DESC;


-- Q16. Professional hosts
SELECT
    host_id,
    host_name,
    COUNT(*) AS listings
FROM airbnb_listings
GROUP BY host_id, host_name
HAVING COUNT(*) >= 10
ORDER BY listings DESC;


-- Q17. Top hosts by number of listings
SELECT
    host_id,
    host_name,
    COUNT(*) AS total_listings
FROM airbnb_listings
GROUP BY host_id, host_name
ORDER BY total_listings DESC
LIMIT 10;


-- Q18. Price category distribution
SELECT
    price_category,
    COUNT(*) AS listings
FROM airbnb_listings
GROUP BY price_category
ORDER BY listings DESC;


-- Q19. Availability category distribution
SELECT
    availability_category,
    COUNT(*) AS listings
FROM airbnb_listings
GROUP BY availability_category
ORDER BY listings DESC;


-- Q20. Listings costing more than $300
SELECT
    COUNT(*) AS expensive_listings
FROM airbnb_listings
WHERE price_usd > 300;


-- Q21. Average price by property type
SELECT
    property_type,
    COUNT(*) AS listings,
    ROUND(AVG(price_usd), 2) AS avg_price
FROM airbnb_listings
GROUP BY property_type
ORDER BY avg_price DESC;


-- Q22. Revenue by borough
SELECT
    borough,
    ROUND(SUM(estimated_annual_revenue_usd), 2) AS estimated_revenue
FROM airbnb_listings
GROUP BY borough
ORDER BY estimated_revenue DESC;


-- Q23. Revenue by room type
SELECT
    room_type,
    ROUND(SUM(estimated_annual_revenue_usd), 2) AS estimated_revenue
FROM airbnb_listings
GROUP BY room_type
ORDER BY estimated_revenue DESC;


-- Q24. Top 10 listings by estimated revenue
SELECT
    listing_id,
    listing_name,
    borough,
    room_type,
    price_usd,
    estimated_annual_revenue_usd
FROM airbnb_listings
ORDER BY estimated_annual_revenue_usd DESC
LIMIT 10;


-- Q25. Borough + room type analysis
SELECT
    borough,
    room_type,
    COUNT(*) AS listings,
    ROUND(AVG(price_usd), 2) AS avg_price,
    ROUND(AVG(review_score), 2) AS avg_rating,
    ROUND(AVG(availability_365), 2) AS avg_availability,
    ROUND(SUM(estimated_annual_revenue_usd), 2) AS estimated_revenue
FROM airbnb_listings
GROUP BY borough, room_type
ORDER BY estimated_revenue DESC;