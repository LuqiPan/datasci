SELECT count(*) FROM (
  SELECT DISTINCT docid
  FROM (
    SELECT docid
    FROM frequency
    WHERE term = "transactions"
    INTERSECT
    SELECT docid
    FROM frequency
    WHERE term = "world"
  )
);
