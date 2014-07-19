SELECT COUNT(*) FROM (
  SELECT *
  FROM frequency
  GROUP BY docid
  HAVING sum(count) > 300
);
