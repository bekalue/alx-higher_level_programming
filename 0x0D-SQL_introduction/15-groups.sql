-- lists the number of records with the same score
SELECT score , count(score) AS number GROUP BY score WHERE score ASC;
