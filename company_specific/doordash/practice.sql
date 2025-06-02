-- merchant segmentation by delivery
-- sql to query merchants based on delivery radius < 6, 6 - 10, > 10

SELECT
    CASE
        WHEN radius < 6 THEN 'LESS THAN 6'
        WHEN radius > 6 AND radius < 10 THEN 'BETWEEN 6 AND 10'
        WHEN radius > 10 THEN 'MORE THAN 10'
    END AS radius_segment
,   COUNT(1) AS merchant_count
FROM radius_table
GROUP BY 1;

-- percentage of veg only restaurants
WITH veggie_ratio AS (
    SELECT
        m.id,
        sum(im.is_veg_only) as is_veg,
        sum(case when im.is_veg_only = 0 then 1 else 0 end) as is_not_veg
    FROM
        merchants m
    INNER JOIN m on m.id = mu.merchant_id
        AND m.is_active_flg = 1 AND mu.is_active_flg = 1
    INNER JOIN items im on mu.id = im.menu_id
    GROUP BY 1
)

SELECT
    ROUND((sum(case when is_veg != 0 and is_non_veg = 0 then 1 else 0 end) * 100)/ count(1), 2)
    as percentage_veg_restaurants
FROM veggie_ratio


