CREATE TABLE IF NOT EXISTS books(bid int, uid string, rating int, ts string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INPATH '/home/hadoop/Books.csv' OVERWRITE INTO TABLE books;

CREATE TABLE bookAvg3 AS
SELECT bid, avg(rating) AS avg
FROM books
GROUP BY bid;

SELECT count(bid)
FROM bookAvg3
WHERE avg>=1.0 AND avg<2.0;

SELECT count(bid)
FROM bookAvg3
WHERE avg>=2.0 AND avg<3.0;

SELECT count(bid)
FROM bookAvg3
WHERE avg>=3.0 AND avg<4.0;

SELECT count(bid)
FROM bookAvg3
WHERE avg>=4.0 AND avg<5.0;

SELECT count(bid)
FROM bookAvg3
WHERE avg>=5.0;

CREATE TABLE user_count AS
SELECT count(bid)
FROM books
GROUP BY uid;