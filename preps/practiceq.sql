-- table definition (DDL) for the two tables
CREATE TABLE visits (
  visit_date DATE,
  visit_id INT,
  visitor_id INT,
  num_pages INT
);

CREATE TABLE visitors (
  visitor_id INT,
  user_name VARCHAR(255)
);

-- for each, visitor with max visits. select lexicographically, when visits are equal

WITH
	DAILYCOUNTS AS (
      SELECT
      	visit_date, visitor_id, count(*) as dailycount
      FROM
      	visits
      GROUP BY
      	visit_date, visitor_id
),
VISITORRANKS AS (
  DC.visit_date, V.visitor_id, V.user_name,
  RANK() OVER (PARTITION BY
               	DC.visit_date
               ORDER BY
               	DC.dailycount DESC, V.user_name) AS ranking
  FROM DAILYCOUNTS DC
  JOIN visitors V USING (visitor_id)
 )
 SELECT
 FINAL.visit_date as REPORTDATE,
 FINAL.visitor_id AS VISITORID,
 FINAL.user_name AS USER
 FROM VISITORRANKS FINAL
 WHERE ranking = 1
 ORDER BY FINAL.visit_date
 ;

-- 3 day moving average of the total pages viewed, calculated for each day
SELECT
    visit_date,
    ROUND((SUM(num_pages) OVER (ORDER BY visit_date FROM BETWEEN 2 PRECEDING AND CURRENT ROW)) / 3, 0)
FROM
    (
        SELECT
            visit_date,
            SUM(num_pages) as sum_pages
        FROM visits
        GROUP BY visit_date
    )

-- everyday visitor count
WITH
    VISITSEVERYDAY AS (
        SELECT
            visit_date,
            visitor_id,
            DENSE_RANK() OVER (ORDER BY visit_date) as visit_rank,
            DENSE_RANK() OVER (PARTITION BY visitor_id ORDER BY visit_date) AS visitor_rank
        FROM
            visits
    )
SELECT
    visit_date AS visited-date,
    COUNT(DISTINCT visitor_id) as visitor-count
FROM
    VISITSEVERYDAY
WHERE
    visit_rank = visitor_rank
GROUP BY visit_date
;